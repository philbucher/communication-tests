import unittest
import sys, os

import communication_tests

@unittest.skipUnless(communication_tests.MPI_enabled, "MPI is not enabled!")
class TestMPICommunication(unittest.TestCase):
    def test_dummy(self):
        pass


if __name__ == '__main__':
    unittest.main()
