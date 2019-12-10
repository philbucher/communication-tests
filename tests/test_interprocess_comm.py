import unittest
from base_communication_test import WrapperClass
import communication_tests

@unittest.skipUnless(communication_tests.Interprocess_enabled, "Interprocess is not enabled!")
class TestInterprocessCommunication(WrapperClass.BaseCommunicationTest):
    @classmethod
    def CreateCommunication(cls, connection_name, is_connection_master):
        cls.skipTest("not implemented yet", "not implemented yet")
        return communication_tests.InterprocessCommunication(connection_name, is_connection_master)


if __name__ == '__main__':
    unittest.main()
