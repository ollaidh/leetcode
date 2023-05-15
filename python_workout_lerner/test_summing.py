import unittest


def mysum(*args):
    if not args:
        return args
    result = args[0]
    for arg in args[1:]:
        result += arg
    return result


def add_item_todict(dct: dict, key, value):
    if key not in dct:
        dct[key] = value
    else:
        dct[key] = list(dct[key])
        dct[key].append(value)
    return dct


def combine_dicts(*dicts):
    for dct in dicts[1:]:
        for key, value in dct.items():
            add_item_todict(dicts[0], key, value)
    return dicts[0]


class TestMysum(unittest.TestCase):
    def test_mysum(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], mysum([1, 2], [3, 4], [5, 6]))
        self.assertEqual(10, mysum(1, 4, 5))
        self.assertEqual([1, 2, 3, 'a', 'b', 'c'], mysum([1, 2, 3], ['a', 'b', 'c']))
        self.assertEqual('abcd', mysum('a', 'b', 'c', 'd'))

    def test_add_item_todict(self):
        self.assertEqual({1: ['a', 'b'], 2: 'b', 3: 'c'}, add_item_todict({1: 'a', 2: 'b', 3: 'c'}, 1, 'b'))

    def test_combine_dicts(self):
        self.assertEqual({1: ['a', 'aa'], 2: 'b', 3: 'c', 4: ['d', 'dd'], 5: 'e'},
                         combine_dicts({1: 'a', 2: 'b'}, {3: 'c', 4: 'd', 1: 'aa'}, {5: 'e', 4: 'dd'}))


if __name__ == '__main__':
    unittest.main()