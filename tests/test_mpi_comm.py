import unittest
from base_communication_test import WrapperClass
import communication_tests

@unittest.skipUnless(communication_tests.MPI_enabled, "MPI is not enabled!")
class TestMPICommunication(WrapperClass.BaseCommunicationTest):
    @classmethod
    def CreateCommunication(cls, connection_name, is_connection_master):
        cls.skipTest("not implemented yet", "not implemented yet")
        return communication_tests.MPICommunication(connection_name, is_connection_master)


if __name__ == '__main__':
    unittest.main()
