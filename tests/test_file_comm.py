import unittest
import sys, os, shutil

import communication_tests

class TestFileCommUtilities(unittest.TestCase):
    dir_name = "my_dir"
    file_name = "the_file.dat"
    file_in_dir_name = os.path.join(dir_name,file_name)

    def setUp(self):
        self.remove_leftovers

    def tearDown(self):
        self.remove_leftovers

    def remove_leftovers(self):
        if os.path.isdir(TestFileCommUtilities.dir_name):
            shutil.rmtree(TestFileCommUtilities.dir_name)
        if os.path.isfile(TestFileCommUtilities.file_name):
            os.remove(TestFileCommUtilities.file_name)

    def test_create_directory(self):
        if os.path.isdir(TestFileCommUtilities.dir_name):
            shutil.rmtree(TestFileCommUtilities.dir_name)

        self.assertFalse(os.path.isdir(TestFileCommUtilities.dir_name))
        communication_tests.FileCommUtils.create_directory(TestFileCommUtilities.dir_name)
        self.assertTrue(os.path.isdir(TestFileCommUtilities.dir_name))
        shutil.rmtree(TestFileCommUtilities.dir_name)

    def test_remove_file(self):
        if os.path.isfile(TestFileCommUtilities.file_name):
            os.remove(TestFileCommUtilities.file_name)

        with open(TestFileCommUtilities.file_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isfile(TestFileCommUtilities.file_name))
        communication_tests.FileCommUtils.remove(TestFileCommUtilities.file_name)
        self.assertFalse(os.path.isdir(TestFileCommUtilities.file_name))

    def test_remove_empty_dir(self):
        if os.path.isdir(TestFileCommUtilities.dir_name):
            shutil.rmtree(TestFileCommUtilities.dir_name)
        os.mkdir(TestFileCommUtilities.dir_name)

        self.assertTrue(os.path.isdir(TestFileCommUtilities.dir_name))
        communication_tests.FileCommUtils.remove(TestFileCommUtilities.dir_name)
        self.assertFalse(os.path.isdir(TestFileCommUtilities.dir_name))

    def test_remove_full_dir(self):
        if os.path.isdir(TestFileCommUtilities.dir_name):
            shutil.rmtree(TestFileCommUtilities.dir_name)
        os.mkdir(TestFileCommUtilities.dir_name)

        with open(TestFileCommUtilities.file_in_dir_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isdir(TestFileCommUtilities.dir_name))
        self.assertTrue(os.path.isfile(TestFileCommUtilities.file_in_dir_name))
        with self.assertRaisesRegex(RuntimeError, "not empty"):
            communication_tests.FileCommUtils.remove(TestFileCommUtilities.dir_name)

        communication_tests.FileCommUtils.remove_all(TestFileCommUtilities.dir_name)
        self.assertFalse(os.path.isdir(TestFileCommUtilities.dir_name))

    def test_FileExists(self):
        pass

    def test_Rename(self):
        pass


class TestFileCommunication(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
