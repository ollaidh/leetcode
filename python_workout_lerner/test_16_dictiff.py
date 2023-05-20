import unittest


def dictiff(dict1: dict, dict2: dict) -> dict:
    result = {}
    keys = dict1.keys() | dict2.keys()
    for key in keys:
        if dict1.get(key) != dict2.get(key):
            result[key] = [dict1.get(key), dict2.get(key)]

    return result


def merge_dicts(*dicts: dict) -> dict:
    result = {}
    for d in dicts:
        result.update(d)

    return result


class TestDictiff(unittest.TestCase):
    def test_dictiff(self):
        self.assertEqual({}, dictiff(
            {'a': 1, 'b': 2, 'c': 3},
            {'a': 1, 'b': 2, 'c': 3}))
        self.assertEqual({'c': [3, 4]}, dictiff(
            {'a': 1, 'b': 2, 'c': 3},
            {'a': 1, 'b': 2, 'c': 4}))
        self.assertEqual({'c': [None, 4], 'd': [3, None]}, dictiff(
            {'a': 1, 'b': 2, 'd': 3},
            {'a': 1, 'b': 2, 'c': 4}))
        self.assertEqual({'c': [3, None], 'd': [None, 4]}, dictiff(
            {'a': 1, 'b': 2, 'c': 3},
            {'a': 1, 'b': 2, 'd': 4}))

    def test_merge_dicts(self):
        self.assertEqual({'a': 1, 'b': 2, 'c': 4, 'd': 5}, merge_dicts({'a': 1, 'b': 2}, {'c': 4, 'd': 5}))
        self.assertEqual({}, merge_dicts({}, {}))
        self.assertEqual({'a': 1, 'b': 2, 'c': 4}, merge_dicts({}, {'a': 1, 'b': 2, 'c': 4}))


if __name__ == '__main__':
    unittest.main()
