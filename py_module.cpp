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
    bool sockets_enabled = false;
    bool mpi_enabled = false;

    AddFileCommToPython(m);
#ifdef COMM_TESTS_USE_SOCKETS
    AddSocketsCommToPython(m);
    sockets_enabled = true;
#endif
#ifdef COMM_TESTS_USE_MPI
    AddMPICommToPython(m);
    mpi_enabled = true;
#endif

    m.attr("Sockets_enabled") = sockets_enabled;
    m.attr("MPI_enabled") = mpi_enabled;
}