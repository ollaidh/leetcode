import unittest


def encode_nonprintable(line: str) -> str:
    result = []
    for letter in line:
        if 57 >= ord(letter) >= 48 or 90 >= ord(letter) >= 65 or 122 >= ord(letter) >= 97:
            result.append(letter)
        else:
            result.append(f'%{ord(letter)}')

    return ''.join(result)


class TestEncodeNp(unittest.TestCase):
    def test_encode_nonprintable(self):
        self.assertEqual('fa%38ang%33', encode_nonprintable('fa&ang!'))
        self.assertEqual('%95fa%37ang', encode_nonprintable('_fa%ang'))


if __name__ == '__main__':
    unittest.main()
