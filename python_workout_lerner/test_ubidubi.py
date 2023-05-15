import unittest


def ubidubi(word: str) -> str:
    vowels = 'aeiouAEIOU'
    ubied = []
    for letter in word:
        if letter in vowels:
            if letter == letter.lower():
                ubied.append('ub')
            else:
                ubied.append('UB')
        ubied.append(letter)

    return ''.join(ubied)


class TestUbiDubi(unittest.TestCase):
    def test_ubidubi(self):
        self.assertEqual('ubarubamcubo', ubidubi('aramco'))
        self.assertEqual('UBArubamcUBO', ubidubi('AramcO'))


if __name__ == '__main__':
    unittest.main()
