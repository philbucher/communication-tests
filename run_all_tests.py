import platform
execute_mpi_tests = (platform.system() == 'Linux') # MPI-tests can only be executed on linux

print("Executing the MPI-tests:", execute_mpi_tests)