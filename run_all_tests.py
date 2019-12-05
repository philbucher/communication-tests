import unittest
import platform

execute_mpi_tests = (platform.system() == 'Linux') # MPI-tests can only be executed on linux
print("Executing the MPI-tests:", execute_mpi_tests)

from file_comm.tests import test_file_comm
from sockets_comm.tests import test_sockets_comm
if execute_mpi_tests:
    from mpi_comm.tests import test_mpi_comm

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromModule(test_file_comm))
suite.addTests(loader.loadTestsFromModule(test_sockets_comm))
if execute_mpi_tests:
    suite.addTests(loader.loadTestsFromModule(test_mpi_comm))

unittest.TextTestRunner().run(suite)
