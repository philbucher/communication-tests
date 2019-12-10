# Communication Tests

Small collection of tests for the data-exchange in [CoSimulation of Kratos Multiphysics](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/CoSimulationApplication).

Tests can be executed by executing `tests/run_all_tests.py` with python

Currently the following methods are tested / planned:
- File
- Sockets (using Boost ASIO)
- Interprocess (using Boost Interprocess)
- MPI
- MPI with RMA (remote memory access)

## Reference

If you use this repository, please refer to the official GitHub repository:

```
@misc{communication-tests,
  author = "Philipp Bucher",
  title = "communication-tests",
  howpublished = "\url{https://github.com/philbucher/communication-tests}",
}
```

## Used Libraries
- [pybind11](https://github.com/pybind/pybind11) for exposing C++ to python
- [filesystem](https://github.com/gulrak/filesystem) a c++11 implementation of [c++17 filesystem](https://en.cppreference.com/w/cpp/filesystem)