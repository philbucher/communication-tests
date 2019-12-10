import unittest
import sys, os

import communication_tests

@unittest.skipUnless(communication_tests.Interprocess_enabled, "Interprocess is not enabled!")
class TestInterprocessCommunication(unittest.TestCase):
    def test_dummy(self):
        pass


if __name__ == '__main__':
    unittest.main()
