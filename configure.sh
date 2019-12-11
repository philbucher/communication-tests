#!/bin/bash

# Clean
rm -rf build
rm communication_tests_core.cpython*

# Set CXX-Standard
export COMM_TESTS_CXX_STANDARD=11

# required otherwise doesn't find MPI-symbols
export CC=mpicc
export CXX=mpic++

# Build
cmake -H"." -B"build" \
    -DBUILD_MPI_COMM=ON \
    -DBUILD_SOCKETS_COMM=ON \
    -DBUILD_INTERPROCESS_COMM=ON

cmake --build "build" --target install

echo "\nRunning tests ...\n"
python3 tests/run_all_tests.py