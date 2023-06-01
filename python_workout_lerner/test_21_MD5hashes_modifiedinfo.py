import glob
import unittest
from pathlib import Path
import hashlib
from datetime import datetime
import re


def md5_hashes(folderpath: Path) -> dict:
    # given a folder with text files, returns dictionary:
    # key - file name, value - MD5 hash of file
    files = glob.iglob(str(folderpath) + '/*')
    result = {Path(f).name: hashlib.md5(f.encode()).hexdigest() for f in files}

    return result


def directory_last_modified(folderpath: Path) -> (dict, dict):
    # given a folder with files, returns when the folder and files were last modified:
    # 2 dicts with key - file/folder name, value - time of modification
    folder_info = {}
    files_info = {}
    folder_change_sec = folderpath.stat().st_mtime
    folder_info[str(folderpath)] = datetime.fromtimestamp(folder_change_sec).strftime("%A, %B %d, %Y %I:%M:%S")
    files = glob.iglob(str(folderpath) + '/*')
    for f in files:
        files_time_sec = Path(f).stat().st_mtime
        files_info[Path(f).name] = datetime.fromtimestamp(files_time_sec).strftime("%A, %B %d, %Y %I:%M:%S")

    return folder_info, files_info


class TestHashes(unittest.TestCase):
    def test_md5_hashes(self):
        folderpath = Path(__file__).parent.resolve() / '21_textfiles_test'

        hashes_result = md5_hashes(folderpath)
        self.assertEqual(5, len(hashes_result))
        for _, value in hashes_result.items():
            self.assertTrue(re.match('[0-9a-f]', value))

        times_result = directory_last_modified(folderpath)
        self.assertEqual(2, len(times_result))
        self.assertEqual(5, len(times_result[1]))


if __name__ == '__main__':
    unittest.main()
