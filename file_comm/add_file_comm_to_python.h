#include <pybind11/pybind11.h>

#include "file_comm_utils.h"

void AddFileCommToPython(pybind11::module& m)
{
    auto m_file_comm_utils = m.def_submodule("FileCommUtils");

    m_file_comm_utils.def("CreateDirectory", &FileCommUtils::CreateDirectory);
    m_file_comm_utils.def("Rename",          &FileCommUtils::Rename);
    m_file_comm_utils.def("Remove",          &FileCommUtils::Remove);
    m_file_comm_utils.def("RemoveAll",       &FileCommUtils::RemoveAll);
}