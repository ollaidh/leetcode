import glob
import os
import unittest
import pathlib


def get_size_kb(filepath: str) -> float:
    size_b = os.stat(filepath).st_size
    return round(size_b/1024, 1)


def get_files_size(filepath: pathlib.Path) -> dict:
    files = glob.glob(str(filepath) + '/*')
    files_info = {pathlib.Path(f).name: get_size_kb(f) for f in files if os.path.isfile(f)}
    print(files_info)

    return files_info


class TestFilesReports(unittest.TestCase):
    def test_get_files_size(self):
        file_path = pathlib.Path(__file__).parent.resolve() / 'files_size_test'
        self.assertEqual(
            {'wcfile.txt': 0.2, 'sentences.txt': 0.2, 'passwds.txt': 5.5},
            get_files_size(file_path)
        )


if __name__ == '__main__':
    unittest.main()
