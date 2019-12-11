import unittest

class WrapperClass(object):
    # wrapping in an extra class to avoid discovery of the base-test
    # see https://stackoverflow.com/a/25695512
    class BaseCommunicationTest(unittest.TestCase):

        @classmethod
        def CreateCommunication(cls, connection_name, is_connection_master):
            raise NotImplementedError('"CreateCommunication" has to implemented in the derived class!')

        # def setUp(self):
        #     master_comm = self.CreateCommunication("abc", True)

        def test_connect_disconnect(self):
            pass

        def test_connect_without_disconnect(self):
            # this should perform automatic disconnection, NOT crash!
            pass

        def test_send_receive_int_once_small(self):
            pass

        def test_send_receive_double_once_small(self):
            pass

        def test_send_receive_int_once_large(self):
            pass

        def test_send_receive_double_once_large(self):
            pass

        def test_send_receive_int_multiple_times_small(self):
            pass

        def test_send_receive_double_multiple_times_small(self):
            pass

        def test_send_receive_int_multiple_times_large(self):
            pass

        def test_send_receive_double_multiple_times_large(self):
            pass
