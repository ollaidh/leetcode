import glob
import unittest
import pathlib
from os.path import isfile, getsize


def get_files_size(filepath: pathlib.Path) -> dict:
    files = glob.glob(str(filepath) + '/*')
    files_info = {pathlib.Path(f).name: getsize(f) for f in files if isfile(f)}

    return files_info


class TestFilesReports(unittest.TestCase):
    def test_get_files_size(self):
        file_path = pathlib.Path(__file__).parent.resolve() / 'files_size_test'
        self.assertEqual(
            {'wcfile.txt': 165, 'sentences.txt': 211, 'passwds.txt': 5631},
            get_files_size(file_path)
        )


if __name__ == '__main__':
    unittest.main()
