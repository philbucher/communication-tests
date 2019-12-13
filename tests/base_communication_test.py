import unittest
import communication_tests
import os
from time import sleep
import threading

file_name_to_slave = "signal_to_slave.dat"
file_name_from_slave = "signal_from_slave.dat"

# map signal - [size, case-Id]
# NOTE needs to be consistent with C++
signal_map = {
    "data_0" : 25,
    "data_1" : 25,
    "data_2" : 25,
    "data_3" : 25,
    "data_4" : 1E7,
    "data_5" : 1E7,
    "data_6" : 1E7,
    "data_7" : 1E7,
}

class WrapperClass(object):
    # wrapping in an extra class to avoid discovery of the base-test
    # see https://stackoverflow.com/a/25695512
    class BaseCommunicationTest(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            # making sure there are no leftovers
            RemoveLeftoverFiles()

            if not communication_tests.MPI.IsMPIRun():
                # this is only required in serial
                # in MPI this is started by a different (MPI-)process
                cls.sender = BaseCommunicationTestDataSender()
                cls.sender.ExecuteInThread()

        def setUp(self):
            self.connection_name = "CommunicationTest_{}_{}".format(self.comm_name, self._testMethodName)
            self.master_comm = getattr(communication_tests, self.comm_name)(self.connection_name, True) # true means master
            self.__CommunicateSignalToSlaveProcess(self.connection_name, self.comm_name, "connect")
            self.master_comm.Connect()

        def test_connect_disconnect(self):
            # things are done in setup & tear-down
            pass

        def test_send_receive_int_once_small(self):
            self.__ExecuteSendTest("data_0")

        def test_send_receive_double_once_small(self):
            self.__ExecuteSendTest("data_1")

        def test_send_receive_int_once_large(self):
            self.__ExecuteSendTest("data_2")

        def test_send_receive_double_once_large(self):
            self.__ExecuteSendTest("data_3")

        def test_send_receive_int_multiple_times_small(self):
            self.__ExecuteSendTestMultiple("data_4")

        def test_send_receive_double_multiple_times_small(self):
            self.__ExecuteSendTestMultiple("data_5")

        def test_send_receive_int_multiple_times_large(self):
            self.__ExecuteSendTestMultiple("data_6")

        def test_send_receive_double_multiple_times_large(self):
            self.__ExecuteSendTestMultiple("data_7")

        def __ExecuteSendTestMultiple(self, data_signal):
            for _ in range(100):
                self.__ExecuteSendTest(data_signal)

        def __ExecuteSendTest(self, data_signal):
            self.__CommunicateSignalToSlaveProcess(self.connection_name, self.comm_name, data_signal)
            data_size = signal_map[data_signal]
            self.master_comm.Receive(int(data_size), int(data_signal[5:]))


        @classmethod
        def __CommunicateSignalToSlaveProcess(cls, connection_name, comm_name, signal):
            if not communication_tests.MPI.IsMPIRun():
                print("isAlive:", cls.sender.my_thread.isAlive())
            WaitForFileToBeRemoved(file_name_to_slave)

            with open("."+file_name_to_slave, 'w') as signal_file:
                signal_file.write(connection_name)
                signal_file.write("\n")
                signal_file.write(comm_name)
                signal_file.write("\n")
                signal_file.write(signal)
            os.rename("."+file_name_to_slave, file_name_to_slave) # making "visible"

        def tearDown(self):
            self.__CommunicateSignalToSlaveProcess(self.connection_name, self.comm_name, "disconnect")
            self.master_comm.Disconnect()

        @classmethod
        def tearDownClass(cls):
            cls.__CommunicateSignalToSlaveProcess("dummy", "dummy", "exit")
            if not communication_tests.MPI.IsMPIRun():
                cls.sender.JoinThread()


class BaseCommunicationTestDataSender(object):
    # this class works as the "Sender" of data, the class above is the receiver
    def __init__(self):
        self.my_thread = None

    def Execute(self):
        sleep(1) # giving the other process time to clean leftover files
        self.slave_comm = None
        self.current_connection_name = ""
        self.current_comm_name = ""

        while True:
            read_signal_info = ReceiveSignalFromMasterProcess()
            connection_name = read_signal_info[0]
            comm_name = read_signal_info[1]
            signal = read_signal_info[2]

            if signal == "connect":
                if self.slave_comm is not None:
                    raise Exception("connection exists already")

                self.slave_comm = getattr(communication_tests, comm_name)(connection_name, False) # False means slave
                self.slave_comm.Connect()
                self.current_comm_name = comm_name
                self.current_connection_name = connection_name

            elif signal == "disconnect":
                self.__CheckConnection(connection_name, comm_name)
                self.slave_comm.Disconnect()
                self.slave_comm = None

            elif signal == "exit":
                self.slave_comm = None
                break

            elif signal in signal_map:
                self.__CheckConnection(connection_name, comm_name)
                data_size = signal_map[signal]
                self.slave_comm.Send(int(data_size), int(signal[5:]))

            else:
                raise Exception('Signal "{}" not recognized!'.format(signal))

    def ExecuteInThread(self):
        self.my_thread = threading.Thread(target=self.Execute)
        self.my_thread.start()

    def JoinThread(self):
        self.my_thread.join()

    def __CheckConnection(self, connection_name, comm_name):
        if self.slave_comm is None:
            raise Exception("no connection exists")
        if connection_name != self.current_connection_name:
            raise Exception("Mismatch in connection name")
        if comm_name != self.current_comm_name:
            raise Exception("Mismatch in comm name")


def WaitForFile(file_name):
    while(not os.path.isfile(file_name) or not os.access(file_name, os.R_OK)):
        sleep(0.0001)
    # print("os.access(file_name, os.R_OK)", os.access(file_name, os.R_OK))

def WaitForFileToBeRemoved(file_name):
    while(os.path.isfile(file_name)):
        sleep(0.0001)

def RemoveLeftoverFiles():
    def TryToRemoveFile(file_name):
        try:
            os.remove(file_name)
        except:
            pass
    TryToRemoveFile(file_name_to_slave)
    TryToRemoveFile(file_name_from_slave)

def ReceiveSignalFromMasterProcess():
    WaitForFile(file_name_to_slave)

    with open(file_name_to_slave, 'r') as signal_file:
        read_signal_info = signal_file.read().splitlines()

    if not len(read_signal_info) == 3:
        raise Exception("Wrong signal received:", read_signal_info)

    os.remove(file_name_to_slave)

    return read_signal_info
