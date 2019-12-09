import unittest
import os

loader = unittest.TestLoader()
tests = loader.discover(os.path.dirname(__file__)) # automatically discover all tests in this directory
testRunner = unittest.runner.TextTestRunner(verbosity=1)
return testRunner.run(tests)