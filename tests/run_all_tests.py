import unittest
import os, sys

import communication_tests
if communication_tests.MPI.Rank() == 0:
    communication_tests.CompilerInfo()
    print()

communication_tests.MPI.Barrier()

is_slave_process = (("--tests-slave" in sys.argv[1:]) or (communication_tests.MPI.Rank() == 1))

if is_slave_process:
    from base_communication_test import BaseCommunicationTestDataSender
    BaseCommunicationTestDataSender().Execute()
else:
    loader = unittest.TestLoader()
    tests = loader.discover(os.path.dirname(__file__)) # automatically discover all tests in this directory
    testRunner = unittest.runner.TextTestRunner(verbosity=1)
    sys.exit(not testRunner.run(tests).wasSuccessful())