import unittest


def find_first_positive(nums: list[int]):
    left, right = 0, len(nums) - 1
    while (left != right) and (right != left + 1):
        mid = (left + right) // 2
        if nums[mid] > 0:
            right = mid
        else:
            left = mid

    if nums[left] > 0:
        return left
    if nums[right] > 0:
        return right
    return len(nums) - 1


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        start_pos = find_first_positive(nums)
        lp, rp = start_pos - 1, start_pos
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
    def test_sortedSquares(self):
        solution = Solution()
        self.assertEqual([0, 1, 9, 16, 100], solution.sortedSquares([-4, -1, 0, 3, 10]))
        self.assertEqual([4, 9, 9, 49, 121], solution.sortedSquares([-7, -3, 2, 3, 11]))
        self.assertEqual([0], solution.sortedSquares([0]))
