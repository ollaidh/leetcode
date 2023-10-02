# There are n kids with candies. You are given an integer array candies,
# where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that you have.
#
# Return a boolean array result of length n, where result[i] is true if,
# after giving the ith kid all the extraCandies, they will have the greatest
# number of candies among all the kids, or false otherwise.
#
# Note that multiple kids can have the greatest number of candies.


import unittest


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]


class TestSolution(unittest.TestCase):
    def test_kidsWithCandies(self):
        solution = Solution()
        self.assertEqual([True,True,True,False,True], solution.kidsWithCandies([2,3,5,1,3], 3))
        self.assertEqual([True,False,False,False,False], solution.kidsWithCandies([4,2,1,1,2], 1))
        self.assertEqual([True,False,True], solution.kidsWithCandies([12,1,12], 10))


if __name__ == "__main__":
    unittest.main()
