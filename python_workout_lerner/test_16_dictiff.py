import unittest
import random
from unittest.mock import patch
from unittest.mock import Mock


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


def args_to_dict(*args) -> dict:
    result = {}
    if len(args) % 2 != 0:
        raise ValueError('Number of arguments is not even!')
    for i in range(0, (len(args) - 1), 2):
        result[args[i]] = args[i + 1]

    return result


def random_bool() -> bool:
    return random.choice([True, False])


def dict_partition(dict_all, function) -> list[dict]:
    dict1, dict2 = {}, {}
    for key, value in dict_all.items():
        if function():
            dict1[key] = value
        else:
            dict2[key] = value
    return [dict1, dict2]


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

    def test_args_to_dict(self):
        self.assertEqual({'b': 1, 'c': 2, 'd': 3}, args_to_dict('b', 1, 'c', 2, 'd', 3))
        self.assertEqual({'b': 1}, args_to_dict('b', 1))
        self.assertRaises(TypeError, args_to_dict, ['b', 1], 2)
        self.assertRaises(ValueError, args_to_dict, 'b')

    @patch('test_16_dictiff.random_bool')
    def test_dict_partition_1(self, bool_mock):
        bool_mock.return_value = True
        self.assertEqual([{'a': 1, 'b': 2, 'c': 4}, {}], dict_partition({'a': 1, 'b': 2, 'c': 4}, random_bool))
        bool_mock.return_value = False
        self.assertEqual([{}, {'a': 1, 'b': 2, 'c': 4}], dict_partition({'a': 1, 'b': 2, 'c': 4}, random_bool))
        random_bool_mock = Mock(side_effect=[True, False, False, True, False])
        self.assertEqual([{'a': 1, 'd': 5}, {'b': 2, 'c': 4, 'e': 6}],
                         dict_partition({'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6}, random_bool_mock))

    def test_dict_partition_2(self):
        random_bool_mock = Mock(side_effect=[True, False, False, True, False])
        self.assertEqual([{'a': 1, 'd': 5}, {'b': 2, 'c': 4, 'e': 6}],
                         dict_partition({'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6}, random_bool_mock))


if __name__ == '__main__':
    unittest.main()
