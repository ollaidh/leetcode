# Implement the RandomizedSet class:
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present.
# Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present.
# Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements
# (it's guaranteed that at least one element exists when this method is called).
# Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.


import random
import unittest


class RandomizedSet(object):

    def __init__(self):
        self.numbers = []  # store elements in list in order to use random.choise function which works in O(1) time complexity
        self.index = {}  # in parallel store elements in dictionary (key - element, value - index of element in list)

    def insert(self, val):
        if val in self.index:
            return False
        self.numbers.append(val)
        self.index[val] = len(self.numbers) - 1
        return True

    def remove(self, val):
        if val not in self.index:
            return False
        ind_del = self.index[val]
        self.numbers[ind_del], self.numbers[-1] = self.numbers[-1], self.numbers[ind_del]   # swap in oder tp delete the last element - O(1) complexity
        self.index[self.numbers[ind_del]] = self.index[val]
        self.numbers.pop()
        del self.index[val]
        return True

    def getRandom(self):
        return random.choice(self.numbers)


class TestInsDelRand(unittest.TestCase):
    # def test_create1(self):
    #     rset = RandomizedSet()
    #     self.assertEqual(rset.insert(1), True)
    #     self.assertEqual(rset.remove(2), False)
    #     self.assertEqual(rset.insert(2), True)
    #     self.assertTrue(rset.getRandom() > 0)
    #     self.assertEqual(rset.remove(1), True)
    #     self.assertEqual(rset.insert(2), False)
    #     self.assertEqual(rset.getRandom(), 2)

    # def test_create2(self):
    #     rset = RandomizedSet()
    #     self.assertEqual(rset.insert(0), True)
    #     self.assertEqual(rset.insert(1), True)
    #     self.assertEqual(rset.remove(0), True)
    #     self.assertEqual(rset.insert(2), True)
    #     self.assertEqual(rset.remove(1), True)
    #     self.assertEqual(rset.getRandom(), 2)

    def test_create3(self):
        rset = RandomizedSet()
        self.assertEqual(rset.insert(3), True)
        self.assertEqual(rset.remove(3), True)
        self.assertEqual(rset.remove(0), False)
        self.assertEqual(rset.insert(3), True)
        self.assertEqual(rset.getRandom(), 3)
        self.assertEqual(rset.remove(0), False)


if __name__ == '__main__':
    unittest.main()
