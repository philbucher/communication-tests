#!/bin/bash

# Clean
rm -rf build
rm tests/communication_tests.cpython*

# Build
cmake -H"." -B"build"
cmake --build "build" --target install

echo "\nRunning tests ...\n"
python3 tests/run_all_tests.py