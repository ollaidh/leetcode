import unittest
from collections import Counter


def most_repeated_letter(word: str) -> int:
    if not word:
        return 0
    letters_counted = Counter(word.lower())
    most_freq = max([value for _, value in letters_counted.items()])
    return most_freq


def most_repeated_vowel(word: str) -> int:
    if not word:
        return 0
    letters_counted = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letter in word:
        if letter.lower() in letters_counted:
            letters_counted[letter.lower()] += 1
    most_freq = max([value for _, value in letters_counted.items()])
    return most_freq


def word_most_repeated_character(seq: tuple | list, func) -> str:
    if not seq:
        return ''
    result = seq[0]
    most_freq = func(result)
    for word in seq[1:]:
        if func(word) > most_freq:
            most_freq = func(word)
            result = word
    return result


def word_most_repeated_letters(seq: tuple | list) -> str:
    return word_most_repeated_character(seq, most_repeated_letter)


def word_most_repeated_vowels(seq: tuple | list) -> str:
    return word_most_repeated_character(seq, most_repeated_vowel)


class TestMRL(unittest.TestCase):
    def test_most_repeated_letter(self):
        self.assertEqual(0, most_repeated_letter(''))
        self.assertEqual(6, most_repeated_letter('aabbbddddddc'))
        self.assertEqual(1, most_repeated_letter('a'))
        self.assertEqual(2, most_repeated_letter('abcabc'))
        self.assertEqual(2, most_repeated_letter('AaBbCc'))
        self.assertEqual(2, most_repeated_letter('hello12344'))

    def test_most_repeated_vowel(self):
        self.assertEqual(0, most_repeated_vowel(''))
        self.assertEqual(2, most_repeated_vowel('aabbbddddddc'))
        self.assertEqual(1, most_repeated_vowel('a'))
        self.assertEqual(2, most_repeated_vowel('abcabc'))
        self.assertEqual(2, most_repeated_vowel('AaBbCc'))
        self.assertEqual(1, most_repeated_vowel('hello12344'))

    def test_word_most_repeated_character(self):
        self.assertEqual('Aaaaaaa', word_most_repeated_letters(['zz', 'xyz', 'Aaaaaaa', 'pasflnkqwhbfkjasl']))
        self.assertEqual('', word_most_repeated_letters([]))
        self.assertEqual('a', word_most_repeated_letters(['a']))


if __name__ == '__main__':
    unittest.main()
