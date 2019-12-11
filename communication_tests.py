from communication_tests_core import *
import os, sys
import atexit

def __ModuleInitDetail():
    mpi_detected = (                         # Probing the environment to see if this is an MPI run
        "OMPI_COMM_WORLD_SIZE" in os.environ # OpenMPI implementation detected
        or "PMI_SIZE" in os.environ          # Intel MPI detected
        or "MPI_LOCALNRANKS" in os.environ   # Recent mpich detected
    )
    mpi_requested = "--using-mpi" in sys.argv[1:] # Forcing MPI initialization through command-line flag

    using_mpi = False
    if mpi_detected or mpi_requested:
        if MPI_enabled:
            # if sys.platform.startswith('linux'):
            #     # Note: from Python 3.3 onwards, dll load flags are available from module os
            #     # from Python 3.6 onwards, module DLFCN no longer exists
            #     flags = sys.getdlopenflags()
            #     if sys.version_info >= (3,3):
            #         dll_load_flags = os.RTLD_NOW | os.RTLD_GLOBAL
            #     else:
            #         import DLFCN as dl
            #         dll_load_flags = dl.RTLD_NOW | dl.RTLD_GLOBAL
            #     sys.setdlopenflags(dll_load_flags)

            #     print("done setting weird flags")

            print("Initializing MPI")
            MPI.InitializeMPI()

            # if sys.platform.startswith('linux'):
            #     # restore default system flags
            #     sys.setdlopenflags(flags)
        else:
            raise Exception("MPI is not enabled!")

def __FinalizeMPI():
    if MPI.IsMPIRun():
        print("Finalizing MPI")
        MPI.FinalizeMPI()

__ModuleInitDetail()
atexit.register(__FinalizeMPI) # this is not the safest way to do, but for this it is sufficient. Kratos does it in a better way
