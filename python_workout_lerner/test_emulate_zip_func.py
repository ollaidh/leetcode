import unittest


def emulate_zip(*itrbls) -> list[tuple]:
    zipped = [[] for _ in range(len(itrbls[0]))]
    for itr in itrbls:
        for ind, element in enumerate(itr):
            zipped[ind].append(element)
    result = [tuple(zp) for zp in zipped]
    return result


class TestEmulateZip(unittest.TestCase):
    def test_emulate_zip(self):
        self.assertEqual([(10, 'a'), (20, 'b'), (30, 'c')], emulate_zip([10, 20, 30], 'abc'))
        self.assertEqual([(10, 'a', 1), (20, 'b', 2), (30, 'c', 3)], emulate_zip([10, 20, 30], 'abc', (1, 2, 3)))


if __name__ == '__main__':
    unittest.main()
