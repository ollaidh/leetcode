import unittest
import pathlib
import dataclasses


@dataclasses.dataclass(kw_only=True)
class FileInfo:
    characters: int
    words: int
    lines: int
    unique_words: int


def new_file_info() -> FileInfo:
    return FileInfo(characters=0, words=0, lines=0, unique_words=0)


def count_file_parameters(filename: pathlib.Path) -> FileInfo:
    file_info = new_file_info()
    with open(filename) as f:
        words = set()
        for line in f:
            file_info.characters += len(line)
            file_info.words += len(line.split())
            file_info.lines += 1
            words.update(set(line.rstrip('\n').split()))
        file_info.unique_words = len(words)

    return file_info


class TestCounters(unittest.TestCase):
    def test_get_final_line(self):
        file_path = pathlib.Path(__file__).parent.resolve() / 'files' / 'wcfile.txt'
        file_info = count_file_parameters(file_path)
        self.assertEqual(28, file_info.words)
        self.assertEqual(20, file_info.unique_words)
        self.assertEqual(11, file_info.lines)
        self.assertEqual(165, file_info.characters)


if __name__ == '__main__':
    unittest.main()
