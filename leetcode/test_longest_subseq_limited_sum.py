# You are given an integer array nums of length n, and an integer array queries of length m.
# Return an array answer of length m where answer[i] is the maximum size of a subsequence
# that you can take from nums such that the sum of its elements is less than or equal to queries[i].


import unittest


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        answer = []
        nums.sort()
        for q in queries:
            curr_length = 0
            curr_sum = 0
            for n in nums:
                if curr_sum + n > q:
                    break
                curr_length += 1
                curr_sum += n
            answer.append(curr_length)
        return answer


class TestAnswerQweries(unittest.TestCase):
    def test_answerQueries(self):
        solution = Solution()
        self.assertEqual(solution.answerQueries([4, 5, 2, 1], [3, 10, 21]), [2, 3, 4])
        self.assertEqual(solution.answerQueries([2, 3, 4, 5], [1]), [0])
        self.assertEqual(solution.answerQueries([1], [1]), [1])
        self.assertEqual(solution.answerQueries([], []), [])


if __name__ == '__main__':
    unittest.main()
