project(communication_tests)
cmake_minimum_required (VERSION 2.8.6)

add_subdirectory(external_libraries/pybind)

file(GLOB_RECURSE COMM_TESTS_PY_SOURCES
    ${CMAKE_SOURCE_DIR}/file_comm/*.cpp
)

if(BUILD_SOCKETS_COMM)
    message("Compiling Sockets-Communication")

    # the following line is required for older versions of boost, see https://stackoverflow.com/questions/9723793/undefined-reference-to-boostsystemsystem-category-when-compiling
    add_definitions(-DBOOST_ERROR_CODE_HEADER_ONLY)

    find_package(Boost)
    include_directories(${BOOST_ROOT})

    file(GLOB_RECURSE COMM_TESTS_PY_SOURCES
        ${COMM_TESTS_PY_SOURCES}
        ${CMAKE_SOURCE_DIR}/sockets_comm/*.cpp
    )
endif()


set(EXTRA_LIBS_TO_LINK "")

if(BUILD_MPI_COMM)
    message("Compiling MPI-Communication")

    find_package(MPI)
    # add_definitions( -DKRATOS_USING_MPI )

    include_directories(SYSTEM ${MPI_INCLUDE_PATH})
    set(EXTRA_LIBS_TO_LINK ${MPI_LIBRARIES})

    file(GLOB_RECURSE COMM_TESTS_PY_SOURCES
        ${COMM_TESTS_PY_SOURCES}
        ${CMAKE_SOURCE_DIR}/mpi_comm/*.cpp
    )

endif()

pybind11_add_module(communication_tests ${COMM_TESTS_PY_SOURCES} ${EXTRA_LIBS_TO_LINK})

install(TARGETS communication_tests DESTINATION ${CMAKE_SOURCE_DIR}/tests)  # installing directly into the tests-dir where it is used, no need to bother with a separate "libs" dir