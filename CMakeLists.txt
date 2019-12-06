project(communication_tests)
cmake_minimum_required (VERSION 2.8.6)

add_subdirectory(external_libraries/pybind)

if(BUILD_SOCKETS_COMM)
    message("Compiling Sockets-Communication")
    add_definitions(-DCOMM_TESTS_USE_SOCKETS)

    # the following line is required for older versions of boost, see:
    # https://stackoverflow.com/questions/9723793/undefined-reference-to-boostsystemsystem-category-when-compiling
    add_definitions(-DBOOST_ERROR_CODE_HEADER_ONLY)

    find_package(Boost)
    include_directories(${BOOST_ROOT})
endif()


set(EXTRA_LIBS_TO_LINK "")

if(BUILD_MPI_COMM)
    message("Compiling MPI-Communication")
    add_definitions(-DCOMM_TESTS_USE_MPI)

    find_package(MPI)

    include_directories(SYSTEM ${MPI_INCLUDE_PATH})
    set(EXTRA_LIBS_TO_LINK ${MPI_LIBRARIES})

endif()

pybind11_add_module(communication_tests py_module.cpp ${EXTRA_LIBS_TO_LINK})

install(TARGETS communication_tests DESTINATION ${CMAKE_SOURCE_DIR}/tests)  # installing directly into the tests-dir where it is used, no need to bother with a separate "libs" dir