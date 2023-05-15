import unittest
import pathlib
import re


def cut_punct(word: str) -> str:
    punct = r'(,|\.|!|\?|;|:)+$'
    new_word = re.sub(punct, '', word)
    return new_word


def make_sentence(file_path: str, sent_n: int) -> str:
    result = []
    with open(file_path) as file:
        nline = 0
        for line in file:
            curr_line = line.split()
            word = curr_line[min(len(curr_line) - 1, nline)]
            word = cut_punct(word)
            result.append(word)
            nline += 1
            if nline >= sent_n:
                break
    return ' '.join(result)


class TestMakeSentence(unittest.TestCase):
    def test_cut_punct(self):
        self.assertEqual('ab!cd', cut_punct('ab!cd?!'))

    def test_make_sentence(self):
        path = pathlib.Path(__file__).parent.resolve()
        self.assertEqual('I is now be are try away', make_sentence(f'{path}/files/sentences.txt', 7))


if __name__ == '__main__':
    unittest.main()
