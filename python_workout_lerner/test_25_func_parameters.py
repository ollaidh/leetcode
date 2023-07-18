import unittest
import pathlib
import os
import glob
import tempfile


def multiplier(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def copyfile(filepath, copy_to_folder_name, *copynames):
    with open(filepath) as copy_from:
        contents = copy_from.read()
        for copy in copynames:
            name = pathlib.Path(filepath).parent.resolve() / copy_to_folder_name / copy
            with open(name, 'w') as copy_to:
                copy_to.write(contents)


def anyjoin(iterable, separator=' ') -> str:
    if len(iterable) == 1:
        return f'{iterable}{separator}'
    result = ''
    for i in range(0, len(iterable) - 1):
        result += f'{str(iterable[i])}{separator}'
    result += str(iterable[-1])
    return result


class TestFuncParameters(unittest.TestCase):
    def test_multiplier(self):
        self.assertEqual(4, multiplier(2, 2))
        self.assertEqual(8, multiplier(2, 2, 2))
        self.assertEqual(10, multiplier(1, 1, 1, 1, 10))
        self.assertEqual(-5, multiplier(-1, 10, 0.5))
        self.assertEqual(11, multiplier(11))

    def test_copyfile(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            inp_folder = pathlib.Path(__file__).parent.resolve() / '25_copy_files'
            inp_file = inp_folder / 'test_file.txt'
            inp_file_size = os.path.getsize(inp_file)
            copyfile(inp_file, tmpdirname, 'test_file_copy1.txt', 'test_file_copy2.txt', 'test_file_copy3.txt')
            result = list(glob.glob(f'{tmpdirname}/*'))
            self.assertEqual(3, len(result))
            with os.scandir(inp_folder) as folder:
                for file in folder:
                    self.assertEqual(inp_file_size, os.path.getsize(file))

    def test_anyjoin(self):
        self.assertEqual("1 2 3", anyjoin([1, 2, 3]))
        self.assertEqual("a**b**c", anyjoin("abc", "**"))
        self.assertEqual("a-z", anyjoin("az", "-"))
        self.assertEqual("a-", anyjoin("a", "-"))



if __name__ == '__main__':
    unittest.main()
