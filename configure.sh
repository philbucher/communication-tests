#!/bin/bash

# Clean
rm -rf build
rm tests/communication_tests.cpython*

# Build
cmake -H"." -B"build" -DBUILD_MPI_COMM=ON -DBUILD_SOCKETS_COMM=ON -DBOOST_ROOT="${HOME}/software/boost/boost_1_67_0"
cmake --build "build" --target install

echo "\nRunning tests ...\n"
python3 tests/run_all_tests.py