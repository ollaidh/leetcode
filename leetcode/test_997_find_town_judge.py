# In a town, there are n people labeled from 1 to n.
# There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing
# that the person labeled ai trusts the person labeled bi.
# If a trust relationship does not exist in trust array,
# then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


import unittest


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trusting = [0] * n
        trusted = [0] * n
        for t in trust:
            trusting[t[0] - 1] += 1
            trusted[t[1] - 1] += 1
        for i in range(n):
            if trusting[i] == 0 and trusted[i] == n - 1:
                return i + 1
        return -1


class TestSolution(unittest.TestCase):
    def test_findJudge(self):
        solution = Solution()
        self.assertEqual(2, solution.findJudge(2, [[1, 2]]))
        self.assertEqual(3, solution.findJudge(3, [[1, 3], [2, 3]]))
        self.assertEqual(-1, solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
        self.assertEqual(-1, solution.findJudge(4, [[1, 3], [2, 3], [3, 1], [4, 3]]))
        self.assertEqual(-1, solution.findJudge(4, [[1, 3], [2, 3], [3, 4]]))
