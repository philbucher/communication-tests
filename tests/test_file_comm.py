import unittest
import sys, os

import communication_tests

class TestFileCommUtilities(unittest.TestCase):

    def test_CreateDirectory(self):
        communication_tests.FileCommUtils.CreateDirectory("TestDir")

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
