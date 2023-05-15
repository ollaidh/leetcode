import unittest


def transpose_strings(matrix: list[list]) -> list[list]:
    rows = len(matrix[0])
    matrix_transp = [[] for i in range(rows)]
    for line in matrix:
        for i, element in enumerate(line):
            matrix_transp[i].append(element)
    return matrix_transp


class TestTranspStr(unittest.TestCase):
    def test_transpose_strings(self):
        self.assertEqual([['abc', 'jkl', 'stu'],
                         ['def', 'mno', 'vwx'],
                         ['ghi', 'pqr', 'yz'],
                          ['eee', 'fff', 'zzz']],
                         transpose_strings([['abc', 'def', 'ghi', 'eee'],
                                            ['jkl', 'mno', 'pqr', 'fff'],
                                            ['stu', 'vwx', 'yz', 'zzz']]))


if __name__ == '__main__':
    unittest.main()

