from pathlib import Path
import unittest
import glob
from test_nonsencial_sentence import cut_punct


def get_longest_word(filepath: Path) -> str:
    # returns the longest word in given file:
    longest_word = ''
    with open(filepath) as f:
        for line in f:
            for word in line.split():
                word_cut = cut_punct(word)
                if len(word_cut) > len(longest_word):
                    longest_word = word_cut

    return longest_word


def get_all_longest_words(filepath: Path) -> dict:
    # given a folder with files, returns a dict, where the key is filename and value is the longest word from the file
    files = glob.iglob(str(filepath) + '/*')
    longest_words = {Path(f).name: get_longest_word(Path(f))
                     for f in files if Path.is_file(Path(f))}
    return longest_words


class TestLongestWords(unittest.TestCase):
    def test_get_longest_word_file(self):
        filepath = Path(__file__).parent.resolve() / 'words_length_test' / '43-0.txt'
        self.assertEqual('ProjectGutenbergEBook', get_longest_word(filepath))
        filepath = Path(__file__).parent.resolve() / 'words_length_test' / '46-0.txt'
        self.assertEqual('ChristmasCarol', get_longest_word(filepath))

    def test_get_all_longest_words(self):
        filepath = Path(__file__).parent.resolve() / 'words_length_test'
        self.assertEqual(
            {'1342-0.txt': 'acknowledgedacknowledged',
             '2701-0.txt': 'combinationcombination',
             '43-0.txt': 'ProjectGutenbergEBook',
             '46-0.txt': 'ChristmasCarol',
             '84-0.txt': 'Wollstonecraft'},
            get_all_longest_words(filepath))


if __name__ == '__main__':
    unittest.main()
