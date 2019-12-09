#pragma once

#if defined(__cplusplus) && __cplusplus >= 201703L && defined(__has_include) && __has_include(<filesystem>)
    #include <filesystem>
    namespace fs = std::filesystem;
    #define FILESYSTEM_AVAILABLE
#else
    #include "../external_libraries/ghc/filesystem.hpp"
    namespace fs = ghc::filesystem;
#endif