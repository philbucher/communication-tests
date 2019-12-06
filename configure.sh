#!/bin/bash

# Clean
rm -rf build
rm tests/communication_tests.cpython*

# Build
cmake -H"." -B"build"
cmake --build "build" --target install