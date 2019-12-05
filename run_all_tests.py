import unittest
import platform
import sys

execute_mpi_tests = (platform.system() == 'Linux') # MPI-tests can only be executed on linux
print("Executing the MPI-tests:", execute_mpi_tests)


sys.path.append("file_comm/tests")
sys.path.append("sockets_comm/tests")
sys.path.append("mpi_comm/tests")
import test_file_comm
import test_sockets_comm
if execute_mpi_tests:
    import test_mpi_comm

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromModule(test_file_comm))
suite.addTests(loader.loadTestsFromModule(test_sockets_comm))
if execute_mpi_tests:
    suite.addTests(loader.loadTestsFromModule(test_mpi_comm))

unittest.TextTestRunner().run(suite)
