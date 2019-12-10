import unittest

class WrapperClass(object):
    # wrapping in an extra class to avoid discovery of the base-test
    # see https://stackoverflow.com/a/25695512
    class BaseCommunicationTest(unittest.TestCase):

        @classmethod
        def CreateCommunication(cls, connection_name, is_connection_master):
            raise NotImplementedError('"CreateCommunication" has to implemented in the derived class!')

        def test_connect_disconnect(self):
            comm_1 = self.CreateCommunication("abc", True)
