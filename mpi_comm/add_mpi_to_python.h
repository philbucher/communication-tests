#pragma once

#include <pybind11/pybind11.h>

#ifdef COMM_TESTS_USE_MPI
#include "mpi.h"
#endif

namespace Helpers {

static bool is_mpi_run = false;

void InitializeMPI()
{
#ifdef COMM_TESTS_USE_MPI
    int argc = 0;
    char** argv = nullptr;

    MPI_Init(&argc, &argv);

    is_mpi_run = true;

    // temp, move from here
    int isInterComm;
    MPI_Comm_test_inter(MPI_COMM_WORLD, &isInterComm);
    std::cout << "MPI_COMM_WORLD : " << MPI_COMM_WORLD << " | is_inter_comm: " << std::boolalpha << bool(isInterComm) << std::endl;
#endif
}

void FinalizeMPI()
{
#ifdef COMM_TESTS_USE_MPI
    MPI_Finalize();
#endif
}

int Size()
{
    int size = 1;
#ifdef COMM_TESTS_USE_MPI
    if (is_mpi_run) { MPI_Comm_size(MPI_COMM_WORLD, &size); }
#endif
    return size;
}

int Rank()
{
    int rank = 0;
#ifdef COMM_TESTS_USE_MPI
    if (is_mpi_run) { MPI_Comm_rank(MPI_COMM_WORLD, &rank); }
#endif
    return rank;
}

void Barrier()
{
#ifdef COMM_TESTS_USE_MPI
    if (is_mpi_run) { MPI_Barrier(MPI_COMM_WORLD); }
#endif
}


} // helpers namespace

void AddMPIToPython(pybind11::module& m)
{
    auto m_mpi = m.def_submodule("MPI");

    m_mpi.def("IsMPIRun", [](){return Helpers::is_mpi_run;});

    m_mpi.def("InitializeMPI", &Helpers::InitializeMPI);
    m_mpi.def("FinalizeMPI",   &Helpers::FinalizeMPI);

    m_mpi.def("Size", &Helpers::Size);
    m_mpi.def("Rank", &Helpers::Rank);
    m_mpi.def("Barrier", &Helpers::Barrier);
}