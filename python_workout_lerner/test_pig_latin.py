import unittest


def pig_latin_word(word):
    vowels = 'aeiouy'
    punctuation = '.,!?:;'

    end_punct = ''
    if word[-1] in punctuation:
        end_punct = word[-1]
        word = word[:-1]
    if word[0].lower() in vowels:
        return f'{word}way{end_punct}'
    return f'{word[1:]}{word[0]}ay{end_punct}'


def pig_latin_sentence(sentence):
    words = sentence.split()
    for i in range(len(words)):
        words[i] = pig_latin_word(words[i])
    return ' '.join(words)


class TestPigLatin(unittest.TestCase):
    def test_pig_latin_word(self):
        self.assertEqual('eatway', pig_latin_word('eat'))
        self.assertEqual('Airway', pig_latin_word('Air'))
        self.assertEqual('olanggay?', pig_latin_word('golang?'))
        self.assertEqual('ythonPay', pig_latin_word('Python'))

    def test_pig_latin_sentence(self):
        self.assertEqual('Eatway yourway teaksay!', pig_latin_sentence('Eat your steak!'))


if __name__ == '__main__':
    unittest.main()
