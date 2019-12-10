project(communication_tests)
cmake_minimum_required (VERSION 2.8.6)

# set(PYBIND11_CPP_STANDARD -std=c++17) not used, kept here as a reminder that pybind might override things!
add_subdirectory(external_libraries/pybind)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

if(${MSVC})
    # required such that "__cplusplus" is set to the correct value
    # see https://devblogs.microsoft.com/cppblog/msvc-now-correctly-reports-__cplusplus/
    # Note: min value is c++14 => 201402L (c++11 does not exist, will also output 201402L)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zc:__cplusplus")
endif()

if(BUILD_SOCKETS_COMM OR BUILD_INTERPROCESS_COMM)
    # the following line is required for older versions of boost, see:
    # https://stackoverflow.com/questions/9723793/undefined-reference-to-boostsystemsystem-category-when-compiling
    add_definitions(-DBOOST_ERROR_CODE_HEADER_ONLY)

    add_definitions(-DBOOST_DATE_TIME_NO_LIB)
    add_definitions(-DBOOST_REGEX_NO_LIB)

    include_directories(external_libraries/boost_1_71_0)
endif()

if(BUILD_SOCKETS_COMM)
    message("Building Sockets-Communication")
    add_definitions(-DCOMM_TESTS_USE_SOCKETS)
endif()

if(BUILD_INTERPROCESS_COMM)
    message("Building Interprocess-Communication")
    add_definitions(-DCOMM_TESTS_USE_INTERPROCESS)
endif()

set(EXTRA_LIBS_TO_LINK "") # required for the MPI-Libs

if(BUILD_MPI_COMM)
    message("Building MPI-Communication")
    add_definitions(-DCOMM_TESTS_USE_MPI)

    find_package(MPI)

    message("MPI version found: " ${MPI_VERSION}) # TODO fix this

    include_directories(SYSTEM ${MPI_INCLUDE_PATH})
    set(EXTRA_LIBS_TO_LINK ${MPI_LIBRARIES})

endif()

pybind11_add_module(communication_tests py_module.cpp ${EXTRA_LIBS_TO_LINK})

# Set c++ standard
if(DEFINED ENV{COMM_TESTS_CXX_STANDARD})
    set(COMM_TESTS_CXX_STANDARD $ENV{COMM_TESTS_CXX_STANDARD})
else()
    set(COMM_TESTS_CXX_STANDARD 11) # default to c++11
endif()
set(COMM_TESTS_CXX_STANDARD_REQUIRED ON)

message("Using CXX_STANDARD: " ${COMM_TESTS_CXX_STANDARD})
set_property(TARGET communication_tests PROPERTY CXX_STANDARD ${COMM_TESTS_CXX_STANDARD})

install(TARGETS communication_tests DESTINATION ${CMAKE_SOURCE_DIR}/tests)  # installing directly into the tests-dir where it is used, no need to bother with a separate "libs" dir