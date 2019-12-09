import unittest
import sys, os, shutil

import communication_tests

class TestFileCommUtilities(unittest.TestCase):

    def test_create_directory(self):
        dir_name = "abc"
        if os.path.isdir(dir_name):
            shutil.rmtree(dir_name)

        self.assertFalse(os.path.isdir(dir_name))
        communication_tests.FileCommUtils.create_directory(dir_name)
        self.assertTrue(os.path.isdir(dir_name))
        shutil.rmtree(dir_name)

    def test_remove_file(self):
        file_name = "fd.kg"
        if os.path.isfile(file_name):
            os.remove(file_name)

        with open(file_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isfile(file_name))
        communication_tests.FileCommUtils.remove(file_name)
        self.assertFalse(os.path.isdir(file_name))

    def test_remove_empty_dir(self):
        dir_name = "fdg"
        if os.path.isdir(dir_name):
            shutil.rmtree(dir_name)
        os.mkdir(dir_name)

        self.assertTrue(os.path.isdir(dir_name))
        communication_tests.FileCommUtils.remove(dir_name)
        self.assertFalse(os.path.isdir(dir_name))

    def test_remove_full_dir(self):
        dir_name = "tzui"
        file_name = os.path.join(dir_name, "test_data.dat")
        if os.path.isdir(dir_name):
            shutil.rmtree(dir_name)
        os.mkdir(dir_name)

        with open(file_name, 'w') as test_file:
            test_file.write("hello")

        self.assertTrue(os.path.isdir(dir_name))
        self.assertTrue(os.path.isfile(file_name))
        with self.assertRaisesRegex(RuntimeError, "Directory not empty:"):
            communication_tests.FileCommUtils.remove(dir_name)

        communication_tests.FileCommUtils.remove_all(dir_name)
        self.assertFalse(os.path.isdir(dir_name))

    def test_FileExists(self):
        pass

    def test_Rename(self):
        pass


class TestFileCommunication(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
