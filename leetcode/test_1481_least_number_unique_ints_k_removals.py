# Given an array of integers arr and an integer k.
# Find the least number of unique integers after removing exactly k elements.


import unittest


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        counters = {}
        for a in arr:
            if a not in counters:
                counters[a] = 0
            counters[a] += 1
        freqs = [[value, key] for key, value in counters.items()]
        freqs.sort(key=lambda x: x[0], reverse=True)
        for i in range(k):
            freqs[-1][0] -= 1
            if freqs[-1][0] == 0:
                freqs.pop()
        return len(freqs)


class TestFindLeastNumOfUniqueInts(unittest.TestCase):
    def test_findLeastNumOfUniqueInts(self):
        soliution = Solution()
        self.assertEqual(1, soliution.findLeastNumOfUniqueInts([5, 5, 4], 1))  # add assertion here
        self.assertEqual(2, soliution.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
