import unittest
import sys, os, shutil

import communication_tests

@unittest.skipIf(communication_tests.MPI.IsMPIRun(), "This test can only be run in serial")
class TestFileSystem(unittest.TestCase):
    dir_name = "my_dir"
    file_name = "the_file.dat"
    file_in_dir_name = os.path.join(dir_name,file_name)

    def setUp(self):
        self.remove_leftovers()

    def tearDown(self):
        self.remove_leftovers()

    def remove_leftovers(self):
        if os.path.isdir(TestFileSystem.dir_name):
            shutil.rmtree(TestFileSystem.dir_name)
        if os.path.isfile(TestFileSystem.file_name):
            os.remove(TestFileSystem.file_name)

    def test_create_directory(self):
        # prepare test
        self.assertFalse(os.path.isdir(TestFileSystem.dir_name))

        # call function to be checked
        communication_tests.FileSystem.create_directory(TestFileSystem.dir_name)

        # preform checks
        self.assertTrue(os.path.isdir(TestFileSystem.dir_name))

    def test_remove_file(self):
        # prepare test
        with open(TestFileSystem.file_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isfile(TestFileSystem.file_name))

        # call function to be checked
        communication_tests.FileSystem.remove(TestFileSystem.file_name)

        # preform checks
        self.assertFalse(os.path.isdir(TestFileSystem.file_name))

    def test_remove_empty_dir(self):
        # prepare test
        os.mkdir(TestFileSystem.dir_name)

        self.assertTrue(os.path.isdir(TestFileSystem.dir_name))

        # call function to be checked
        communication_tests.FileSystem.remove(TestFileSystem.dir_name)

        # preform checks
        self.assertFalse(os.path.isdir(TestFileSystem.dir_name))

    def test_remove_all_multiple_times(self):
        # prepare test
        os.mkdir(TestFileSystem.dir_name)

        self.assertTrue(os.path.isdir(TestFileSystem.dir_name))

        # call function to be checked
        communication_tests.FileSystem.remove_all(TestFileSystem.dir_name)
        # preform checks
        self.assertFalse(os.path.isdir(TestFileSystem.dir_name))

        # now check if the function can be called multiple times
        communication_tests.FileSystem.remove_all(TestFileSystem.dir_name)

        # preform checks
        self.assertFalse(os.path.isdir(TestFileSystem.dir_name))

    def test_remove_full_dir(self):
        # prepare test
        os.mkdir(TestFileSystem.dir_name)

        with open(TestFileSystem.file_in_dir_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isdir(TestFileSystem.dir_name))
        self.assertTrue(os.path.isfile(TestFileSystem.file_in_dir_name))

        # call function to be checked
        with self.assertRaisesRegex(RuntimeError, "not empty"):
            communication_tests.FileSystem.remove(TestFileSystem.dir_name)

        communication_tests.FileSystem.remove_all(TestFileSystem.dir_name)

        # can be called multiple times
        communication_tests.FileSystem.remove_all(TestFileSystem.dir_name)

        # preform checks
        self.assertFalse(os.path.isdir(TestFileSystem.dir_name))

    def test_exists_file(self):
        # call function to be checked
        self.assertFalse(communication_tests.FileSystem.exists(TestFileSystem.file_name))

        # prepare test
        with open(TestFileSystem.file_name, 'w') as test_file:
            test_file.write("hello")

        # call function to be checked
        self.assertTrue(communication_tests.FileSystem.exists(TestFileSystem.file_name))

    def test_exists_directory(self):
        # call function to be checked
        self.assertFalse(communication_tests.FileSystem.exists(TestFileSystem.dir_name))

        # prepare test
        os.mkdir(TestFileSystem.dir_name)

        # call function to be checked
        self.assertTrue(communication_tests.FileSystem.exists(TestFileSystem.dir_name))

    def test_exists_file_in_directory(self):
        # call function to be checked
        self.assertFalse(communication_tests.FileSystem.exists(TestFileSystem.file_in_dir_name))

        # prepare test
        os.mkdir(TestFileSystem.dir_name)

        # call function to be checked
        self.assertFalse(communication_tests.FileSystem.exists(TestFileSystem.file_in_dir_name))

        with open(TestFileSystem.file_in_dir_name, 'w') as test_file:
            test_file.write("hello")

        # call function to be checked
        self.assertTrue(communication_tests.FileSystem.exists(TestFileSystem.file_in_dir_name))

        # cleanup
        shutil.rmtree(TestFileSystem.dir_name)

    def test_rename(self):
        # prepare test
        with open(TestFileSystem.file_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isfile(TestFileSystem.file_name))

        new_file_name = "aassdd" + TestFileSystem.file_name

        # call function to be checked
        communication_tests.FileSystem.rename(TestFileSystem.file_name, new_file_name)

        # preform checks
        self.assertFalse(os.path.isfile(TestFileSystem.file_name))
        self.assertTrue(new_file_name)

        # cleanup
        os.remove(new_file_name)

if __name__ == '__main__':
    unittest.main()
