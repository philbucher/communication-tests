#!/bin/bash

# Clean
rm -rf build
rm tests/communication_tests.cpython*

# Set CXX-Standard
export COMM_TESTS_CXX_STANDARD=11

# Build
cmake -H"." -B"build" \
    -DBUILD_MPI_COMM=ON \
    -DBUILD_SOCKETS_COMM=ON \
    -DBUILD_INTERPROCESS_COMM=ON

cmake --build "build" --target install

echo "\nRunning tests ...\n"
python3 tests/run_all_tests.py