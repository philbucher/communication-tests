from base_communication_test import WrapperClass
import communication_tests

class TestFileCommunication(WrapperClass.BaseCommunicationTest):
    @classmethod
    def CreateCommunication(cls, connection_name, is_connection_master):
        cls.skipTest("not implemented yet", "not implemented yet")
        return communication_tests.FileCommunication(connection_name, is_connection_master)


if __name__ == '__main__':
    unittest.main()
