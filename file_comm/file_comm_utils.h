#pragma once

#include <string>
#include <iostream>
#include "../common.h"

#if defined(__cplusplus) && __cplusplus >= 201703L && defined(__has_include) && __has_include(<filesystem>)
    #include <filesystem>
    namespace fs = std::filesystem;
    #define FILESYSTEM_AVAILABLE
#else
    #include "../external_libraries/ghc/filesystem.hpp"
    namespace fs = ghc::filesystem;
#endif

namespace FileCommUtils {

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

} // namespace FileCommUtils