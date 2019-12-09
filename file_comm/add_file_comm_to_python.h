#include <pybind11/pybind11.h>

#include "file_comm_utils.h"

void AddFileCommToPython(pybind11::module& m)
{
    auto m_file_comm_utils = m.def_submodule("FileCommUtils");

    m_file_comm_utils.def("create_directory", &FileCommUtils::create_directory);
    m_file_comm_utils.def("rename",           &FileCommUtils::rename);
    m_file_comm_utils.def("remove",           &FileCommUtils::remove);
    m_file_comm_utils.def("remove_all",       &FileCommUtils::remove_all);
    m_file_comm_utils.def("rename",           &FileCommUtils::rename);
    m_file_comm_utils.def("exists",           &FileCommUtils::exists);
}