import unittest
import os, sys

import communication_tests
communication_tests.CompilerInfo()

loader = unittest.TestLoader()
tests = loader.discover(os.path.dirname(__file__)) # automatically discover all tests in this directory
testRunner = unittest.runner.TextTestRunner(verbosity=1)
sys.exit(not testRunner.run(tests).wasSuccessful())