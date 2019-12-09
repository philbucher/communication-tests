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

void CreateDirectory(const std::string& rDirectoryName)
{

std::cout << "__cplusplus : " << __cplusplus << std::endl;

#ifdef FILESYSTEM_AVAILABLE
std::cout << "FILESYSTEM_AVAILABLE!!!" << std::endl;
#else
std::cout << "FILESYSTEM NOT AVAILABLE, using GHC::FILESYSTEM!!!" << std::endl;
#endif

fs::create_directory("dddddd");

}


void Remove(const std::string& rName)
{

}


void RemoveAll()
{

}

// void IsDirectory()
// {

// }

bool FileExists()
{
    // I am already now using this, here I want to check what happens if the file is in a subfolder...
    return false;
}

bool Rename()
{
    return false;
}

} // namespace FileCommUtils