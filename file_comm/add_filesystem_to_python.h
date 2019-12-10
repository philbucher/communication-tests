#pragma once

#include <pybind11/pybind11.h>

#include <string>
#include <iostream>
#include "file_comm_file_system.h"

namespace Helpers {

// TODO probably those functions could be directly exposed, but for now I am fine with this solution
// note that the filesystem functions accept filesystem::path, but I want to pass a string
// not sure how this directly in the exposure

void create_directory(const std::string& rDirectoryName)
{
    fs::create_directory(rDirectoryName);
}

void remove(const std::string& rName)
{
    fs::remove(rName);
}

void remove_all(const std::string& rName)
{
    fs::remove_all(rName);
}

bool exists(const std::string& rName)
{
    return fs::exists(rName);
}

void rename(const std::string& rOldName, const std::string& rNewName)
{
    fs::rename(rOldName, rNewName);
}

} // helpers namespace

void AddFilesystemToPython(pybind11::module& m)
{
    auto m_filesystem = m.def_submodule("FileSystem");

    m_filesystem.def("create_directory", &Helpers::create_directory);
    m_filesystem.def("rename",           &Helpers::rename);
    m_filesystem.def("remove",           &Helpers::remove);
    m_filesystem.def("remove_all",       &Helpers::remove_all);
    m_filesystem.def("rename",           &Helpers::rename);
    m_filesystem.def("exists",           &Helpers::exists);
}