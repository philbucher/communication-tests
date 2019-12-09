#pragma once

#include <string>
#include <iostream>
#include "../common.h"

#if __has_include(<filesystem>)
    #include <filesystem>
    namespace fs = std::filesystem;
#else
    #include <experimental/filesystem>
    namespace fs = std::experimental::filesystem;
#endif

namespace FileCommUtils {

void CreateDirectory(const std::string& rDirectoryName)
{

std::cout << "__cplusplus : " << __cplusplus << std::endl;

#ifdef FILESYSTEM_AVAILABLE
std::cout << "FILESYSTEM_AVAILABLE!!!" << std::endl;
#else
std::cout << "NOT!!!!! FILESYSTEM_AVAILABLE!!!" << std::endl;
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