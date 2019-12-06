import unittest
import sys, os

import communication_tests

@unittest.skipUnless(communication_tests.Sockets_enabled, "Sockets is not enabled!")
class TestSocketsCommunication(unittest.TestCase):
    def test_dummy(self):
        pass


if __name__ == '__main__':
    unittest.main()
