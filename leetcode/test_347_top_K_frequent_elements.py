# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.


import unittest


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        max_occurence = 0
        freqs = {}
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)
            max_occurence = max(max_occurence, freqs[num])
        counters = [[] for _ in range(max_occurence + 1)]

        for num, freq in freqs.items():
            counters[freq].append(num)

        result = []

        i = max_occurence
        while len(result) < k:
            result.extend(counters[i])
            i -= 1

        return result


class TestSolution(unittest.TestCase):
    def test_topKFrequent(self):
        solution = Solution()
        self.assertEqual([1, 2], solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
        self.assertEqual([1, 4, 5],
                         sorted(solution.topKFrequent([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7], 3)))
        self.assertEqual([4], solution.topKFrequent([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7], 1))
        self.assertEqual([1], solution.topKFrequent([1], 1))
