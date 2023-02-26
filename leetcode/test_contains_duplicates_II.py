# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.


import unittest


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indices = dict()

        for i, num in enumerate(nums):
            if num in indices:
                diff = i - indices[num]
                if diff <= k:
                    return True
            indices[num] = i
        return False


class Test_Duplicate(unittest.TestCase):
    def test_containsNearbyDuplicate(self):
        solution = Solution()

        self.assertTrue(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
        self.assertTrue(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
        self.assertFalse(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
        self.assertTrue(solution.containsNearbyDuplicate([99, 99], 2))
        self.assertTrue(solution.containsNearbyDuplicate([2, 2], 3))
        self.assertTrue(solution.containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3))


if __name__ == '__main__':
    unittest.main()
