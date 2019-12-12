import unittest
from base_communication_test import WrapperClass
import communication_tests

@unittest.skipUnless(communication_tests.MPI_enabled, "MPI is not enabled!")
@unittest.skip("Not yet implemented")
class TestMPICommunication(WrapperClass.BaseCommunicationTest):
    comm_name = "MPICommunication"

if __name__ == '__main__':
    is_slave_process = (("--tests-slave" in sys.argv[1:]) or (communication_tests.MPI.Rank() == 1))

    if is_slave_process:
        from base_communication_test import BaseCommunicationTestDataSender
        BaseCommunicationTestDataSender().Execute()
    else:
        unittest.main()