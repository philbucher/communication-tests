#pragma once

#include <string>
#include <iostream>
#include "../common.h"

#if defined(__cplusplus) && __cplusplus >= 201703L && defined(__has_include)
    #if __has_include(<filesystem>)
        #include <filesystem>
        namespace fs = std::filesystem;
        #define FILESYSTEM_AVAILABLE
    #elif __has_include(<experimental/filesystem>)
        #include <experimental/filesystem>
        namespace fs = std::experimental::filesystem;
        #define FILESYSTEM_EXPERIMENTAL_AVAILABLE
    #else
        #include "../external_libraries/ghc/filesystem.hpp"
        namespace fs = ghc::filesystem;
    #endif
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
#elif defined(FILESYSTEM_EXPERIMENTAL_AVAILABLE)
std::cout << "EXPERIMENTAL FILESYSTEM_AVAILABLE!!!" << std::endl;
#else
std::cout << "FILESYSTEM_AVAILABLE, using GHC::FILESYSTEM!!!" << std::endl;
#endif

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