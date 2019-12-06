#include <pybind11/pybind11.h>

#include "file_comm/add_file_comm_to_python.h"
#ifdef COMM_TESTS_USE_SOCKETS
#include "sockets_comm/add_sockets_comm_to_python.h"
#endif
#ifdef COMM_TESTS_USE_MPI
#include "mpi_comm/add_mpi_comm_to_python.h"
#endif

PYBIND11_MODULE(communication_tests, m)
{
    AddFileCommToPython(m);
#ifdef COMM_TESTS_USE_SOCKETS
    AddSocketsCommToPython(m);
#endif
#ifdef COMM_TESTS_USE_MPI
    AddMPICommToPython(m);
#endif
}