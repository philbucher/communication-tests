#pragma once

#include <pybind11/pybind11.h>

#include <string>
#include <iostream>

#if defined(__cplusplus) && __cplusplus >= 201703L && defined(__has_include) && __has_include(<filesystem>)
    #include <filesystem>
    namespace fs = std::filesystem;
    #define FILESYSTEM_AVAILABLE
#else
    #include "../external_libraries/ghc/filesystem.hpp"
    namespace fs = ghc::filesystem;
#endif

namespace Helpers {

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

void AddFileCommToPython(pybind11::module& m)
{
    auto m_file_comm_utils = m.def_submodule("FileSystem");

    m_file_comm_utils.def("create_directory", &Helpers::create_directory);
    m_file_comm_utils.def("rename",           &Helpers::rename);
    m_file_comm_utils.def("remove",           &Helpers::remove);
    m_file_comm_utils.def("remove_all",       &Helpers::remove_all);
    m_file_comm_utils.def("rename",           &Helpers::rename);
    m_file_comm_utils.def("exists",           &Helpers::exists);
}