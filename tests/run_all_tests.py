import unittest
import os, sys

loader = unittest.TestLoader()
tests = loader.discover(os.path.dirname(__file__)) # automatically discover all tests in this directory
testRunner = unittest.runner.TextTestRunner(verbosity=1)
sys.exit(testRunner.run(tests) !=1)