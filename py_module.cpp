#include <pybind11/pybind11.h>


#ifdef COMM_TESTS_USE_SOCKETS
#include "sockets_comm/sockets_comm.h"
#endif

#ifdef COMM_TESTS_USE_INTERPROCESS
#include "interprocess_comm/interprocess_comm.h"
#endif

#ifdef COMM_TESTS_USE_MPI
#include "mpi_comm/mpi_comm.h"
#endif

// including after boost/asio because of windows.h => https://stackoverflow.com/questions/9750344/boostasio-winsock-and-winsock-2-compatibility-issue
#include "file_comm/file_comm.h"
#include "file_comm/add_filesystem_to_python.h"
#include "mpi_comm/add_mpi_to_python.h"

template<class TCommunication>
void ExposeCommunication(pybind11::module& m, const std::string& rName)
{
    namespace py = pybind11;
    py::class_<TCommunication, Communication>(m, rName.c_str())
        .def(py::init<const std::string&, const bool>());
}

PYBIND11_MODULE(communication_tests_core, m)
{
    bool sockets_enabled = false;
    bool interprocess_enabled = false;
    bool mpi_enabled = false;

    namespace py = pybind11;
    py::class_<Communication>(m, "Communication")
        .def("Connect",    &Communication::Connect)
        .def("Disconnect", &Communication::Disconnect)
        .def("Send",       &Communication::Send)
        .def("Receive",    &Communication::Receive)
        ;

    AddFilesystemToPython(m);
    AddMPIToPython(m);

    ExposeCommunication<FileCommunication>(m, "FileCommunication");

#ifdef COMM_TESTS_USE_SOCKETS
    ExposeCommunication<SocketsCommunication>(m, "SocketsCommunication");
    sockets_enabled = true;
#endif

#ifdef COMM_TESTS_USE_INTERPROCESS
    ExposeCommunication<InterprocessCommunication>(m, "InterprocessCommunication");
    interprocess_enabled = true;
#endif

#ifdef COMM_TESTS_USE_MPI
    ExposeCommunication<MPICommunication>(m, "MPICommunication");
    mpi_enabled = true;
#endif

    m.attr("Sockets_enabled") = sockets_enabled;
    m.attr("Interprocess_enabled") = interprocess_enabled;
    m.attr("MPI_enabled") = mpi_enabled;

    m.def("CompilerInfo", [](){
        std::cout << "Compilation information: " << std::endl;
        std::cout << "    Output of \"__cplusplus\": " << __cplusplus << std::endl;

        std::cout << "    Filesystem available: ";
        #ifdef FILESYSTEM_AVAILABLE
        std::cout << "YES";
        #else
        std::cout << "NO";
        #endif
        std::cout << std::endl;

        std::cout << "    SocketsComm enabled: ";
        #ifdef COMM_TESTS_USE_SOCKETS
        std::cout << "YES";
        #else
        std::cout << "NO";
        #endif
        std::cout << std::endl;

        std::cout << "    InterprocessComm enabled: ";
        #ifdef COMM_TESTS_USE_INTERPROCESS
        std::cout << "YES";
        #else
        std::cout << "NO";
        #endif
        std::cout << std::endl;

        std::cout << "    MPIComm enabled: ";
        #ifdef COMM_TESTS_USE_MPI
        std::cout << "YES";
        #else
        std::cout << "NO";
        #endif
        std::cout << std::endl;

    });
}