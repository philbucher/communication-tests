#include <pybind11/pybind11.h>

#include "../inc/file_comm_utils.h"

namespace py = pybind11;

PYBIND11_MODULE(communication_tests, m)
{
    auto m_file_comm_utils = m.def_submodule("FileCommUtils");

    m_file_comm_utils.def("CreateDirectory", &FileCommUtils::CreateDirectory);
    m_file_comm_utils.def("Rename",          &FileCommUtils::Rename);
    m_file_comm_utils.def("Remove",          &FileCommUtils::Remove);
    m_file_comm_utils.def("RemoveAll",       &FileCommUtils::RemoveAll);
}