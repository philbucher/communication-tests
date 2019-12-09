import unittest
import sys, os, shutil

import communication_tests

class TestFileCommUtilities(unittest.TestCase):
    dir_name = "my_dir"
    file_name = "the_file.dat"
    file_in_dir_name = os.path.join(dir_name,file_name)

    def setUp(self):
        self.remove_leftovers()

    def tearDown(self):
        self.remove_leftovers()

    def remove_leftovers(self):
        if os.path.isdir(TestFileCommUtilities.dir_name):
            shutil.rmtree(TestFileCommUtilities.dir_name)
        if os.path.isfile(TestFileCommUtilities.file_name):
            os.remove(TestFileCommUtilities.file_name)

    def test_create_directory(self):
        # prepare test
        self.assertFalse(os.path.isdir(TestFileCommUtilities.dir_name))

        # call function to be checked
        communication_tests.FileCommUtils.create_directory(TestFileCommUtilities.dir_name)

        # preform checks
        self.assertTrue(os.path.isdir(TestFileCommUtilities.dir_name))

    def test_remove_file(self):
        # prepare test
        with open(TestFileCommUtilities.file_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isfile(TestFileCommUtilities.file_name))

        # call function to be checked
        communication_tests.FileCommUtils.remove(TestFileCommUtilities.file_name)

        # preform checks
        self.assertFalse(os.path.isdir(TestFileCommUtilities.file_name))

    def test_remove_empty_dir(self):
        # prepare test
        os.mkdir(TestFileCommUtilities.dir_name)

        self.assertTrue(os.path.isdir(TestFileCommUtilities.dir_name))

        # call function to be checked
        communication_tests.FileCommUtils.remove(TestFileCommUtilities.dir_name)

        # preform checks
        self.assertFalse(os.path.isdir(TestFileCommUtilities.dir_name))

    def test_remove_full_dir(self):
        # prepare test
        os.mkdir(TestFileCommUtilities.dir_name)

        with open(TestFileCommUtilities.file_in_dir_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isdir(TestFileCommUtilities.dir_name))
        self.assertTrue(os.path.isfile(TestFileCommUtilities.file_in_dir_name))

        # call function to be checked
        with self.assertRaisesRegex(RuntimeError, "not empty"):
            communication_tests.FileCommUtils.remove(TestFileCommUtilities.dir_name)

        communication_tests.FileCommUtils.remove_all(TestFileCommUtilities.dir_name)

        # can be called multiple times
        communication_tests.FileCommUtils.remove_all(TestFileCommUtilities.dir_name)

        # preform checks
        self.assertFalse(os.path.isdir(TestFileCommUtilities.dir_name))

    def test_exists_file(self):
        # call function to be checked
        self.assertFalse(communication_tests.FileCommUtils.exists(TestFileCommUtilities.file_name))

        # prepare test
        with open(TestFileCommUtilities.file_name, 'w') as test_file:
            test_file.write("hello")

        # call function to be checked
        self.assertTrue(communication_tests.FileCommUtils.exists(TestFileCommUtilities.file_name))

    def test_exists_directory(self):
        # call function to be checked
        self.assertFalse(communication_tests.FileCommUtils.exists(TestFileCommUtilities.dir_name))

        # prepare test
        os.mkdir(TestFileCommUtilities.dir_name)

        # call function to be checked
        self.assertTrue(communication_tests.FileCommUtils.exists(TestFileCommUtilities.dir_name))

    def test_exists_file_in_directory(self):
        # call function to be checked
        self.assertFalse(communication_tests.FileCommUtils.exists(TestFileCommUtilities.file_in_dir_name))

        # prepare test
        os.mkdir(TestFileCommUtilities.dir_name)

        # call function to be checked
        self.assertFalse(communication_tests.FileCommUtils.exists(TestFileCommUtilities.file_in_dir_name))

        with open(TestFileCommUtilities.file_in_dir_name, 'w') as test_file:
            test_file.write("hello")

        # call function to be checked
        self.assertTrue(communication_tests.FileCommUtils.exists(TestFileCommUtilities.file_in_dir_name))

        # cleanup
        shutil.rmtree(TestFileCommUtilities.dir_name)

    def test_rename(self):
        # prepare test
        with open(TestFileCommUtilities.file_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isfile(TestFileCommUtilities.file_name))

        new_file_name = "aassdd" + TestFileCommUtilities.file_name

        # call function to be checked
        communication_tests.FileCommUtils.rename(TestFileCommUtilities.file_name, new_file_name)

        # preform checks
        self.assertFalse(os.path.isfile(TestFileCommUtilities.file_name))
        self.assertTrue(new_file_name)

        # cleanup
        os.remove(new_file_name)


class TestFileCommunication(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
