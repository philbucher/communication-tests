import unittest
from base_communication_test import WrapperClass
import communication_tests

@unittest.skipUnless(communication_tests.Sockets_enabled, "Sockets is not enabled!")
class TestSocketsCommunication(WrapperClass.BaseCommunicationTest):
    @classmethod
    def CreateCommunication(cls, connection_name, is_connection_master):
        cls.skipTest("not implemented yet", "not implemented yet")
        return communication_tests.SocketsCommunication(connection_name, is_connection_master)


if __name__ == '__main__':
    unittest.main()
