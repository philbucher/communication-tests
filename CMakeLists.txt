project(communication_tests)
cmake_minimum_required (VERSION 2.8.6)

add_subdirectory(external_libraries/pybind)

file(GLOB_RECURSE COMM_TESTS_PY_SOURCES
    ${CMAKE_SOURCE_DIR}/file_comm/*.cpp
    ${CMAKE_SOURCE_DIR}/sockets_comm/*.cpp
)

if(UNIX AND NOT APPLE)
    message("Compiling MPI-Communication")
    file(GLOB_RECURSE COMM_TESTS_PY_SOURCES
        ${COMM_TESTS_PY_SOURCES}
        ${CMAKE_SOURCE_DIR}/mpi_comm/*.cpp
    )
endif()

pybind11_add_module(communication_tests ${COMM_TESTS_PY_SOURCES})