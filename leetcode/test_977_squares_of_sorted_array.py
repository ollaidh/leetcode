import unittest


def find_first_positive(nums: list[int]) -> tuple[int, int]:
    left, right = 0, len(nums) - 1
    while (left != right) and (right != left + 1):
        mid = (left + right) // 2
        if nums[mid] > 0:
            right = mid
        else:
            left = mid

    if nums[left] >= 0:
        return left - 1, left
    if nums[right] >= 0:
        return right - 1, right
    return len(nums) - 1, len(nums)


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        lp, rp = find_first_positive(nums)
        while lp >= 0 or rp < len(nums):
            if lp < 0:
                remaining = [num * num for num in nums[rp:]]
                result.extend(remaining)
                break
            elif rp >= len(nums):
                remaining = [num * num for num in nums[0:lp]]
                result.extend(remaining)
                break
            else:
                if abs(nums[lp]) <= abs(nums[rp]):
                    result.append(nums[lp] * nums[lp])
                    lp -= 1
                else:
                    result.append(nums[rp] * nums[rp])
                    rp += 1

        return result


class TestSolution(unittest.TestCase):
    def test_find_first_positive(self):
        self.assertEqual((1, 2), find_first_positive([-4, -1, 0, 3, 10]))
        self.assertEqual((3, 4), find_first_positive([-5, -3, -2, -1]))
        self.assertEqual((-1, 0), find_first_positive([0]))

    def test_sortedSquares(self):
        solution = Solution()
        self.assertEqual([0, 1, 9, 16, 100], solution.sortedSquares([-4, -1, 0, 3, 10]))
        self.assertEqual([4, 9, 9, 49, 121], solution.sortedSquares([-7, -3, 2, 3, 11]))
        self.assertEqual([0], solution.sortedSquares([0]))
        self.assertEqual([1, 4, 9, 25], solution.sortedSquares([-5, -3, -2, -1]))
