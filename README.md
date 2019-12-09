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
  title = "ANurbs",
  howpublished = "\url{https://github.com/philbucher/communication-tests}",
}
```
