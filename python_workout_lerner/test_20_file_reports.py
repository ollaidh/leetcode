import glob
import os
import unittest
import pathlib
from math import isclose


def compare_dict_filesize(files1: dict, files2: dict) -> bool:
    if len(files1) != len(files2):
        return False
    for key, value in files1.items():
        if key not in files2:
            return False
        if not isclose(value, files2[key], rel_tol=0.07):
            return False
    return True


def get_files_size(filepath: pathlib.Path) -> dict:
    files = glob.glob(str(filepath) + '/*')
    files_info = {pathlib.Path(f).name: os.stat(f).st_size for f in files if os.path.isfile(f)}

    return files_info


class TestFilesReports(unittest.TestCase):
    def test_compare_dict_filesize(self):
        self.assertTrue(compare_dict_filesize({'a': 10, 'b': 20, 'c': 30}, {'a': 10, 'b': 20.5, 'c': 30}))
        self.assertTrue(compare_dict_filesize({'a': 10, 'b': 20, 'c': 30}, {'a': 10, 'b': 20, 'c': 30}))
        self.assertFalse(compare_dict_filesize({'a': 10, 'b': 20, 'c': 30}, {'a': 100, 'b': 20.5, 'c': 30}))
        self.assertFalse(compare_dict_filesize({'a': 10, 'b': 20, 'c': 30}, {'a': 10, 'b': 20.5}))
        self.assertFalse(compare_dict_filesize({'a': 10, 'b': 20, 'c': 30}, {'a': 10, 'b': 20.5, 'd': 30}))

    def test_get_files_size(self):
        file_path = pathlib.Path(__file__).parent.resolve() / 'files_size_test'
        self.assertTrue(compare_dict_filesize(
            {'wcfile.txt': 165, 'sentences.txt': 211, 'passwds.txt': 5631},
            get_files_size(file_path))
        )


if __name__ == '__main__':
    unittest.main()
