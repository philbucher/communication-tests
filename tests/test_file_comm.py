import unittest
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../libs"))

import communication_tests

class TestFileCommUtilities(unittest.TestCase):

    def test_CreateDirectory(self):
        pass

    def test_Remove(self):
        pass

    def test_RemoveAll(self):
        pass

    def test_FileExists(self):
        pass

    def test_Rename(self):
        pass


class TestFileCommunication(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()