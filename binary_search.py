# Given an array of integers nums which is sorted in ascending order, and an integer
# target, write a function to search target in nums.\
# If target exists, then return its index.Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


import my_utils.testing as test


class Solution(object):
    def search(self, nums, target):

        l, r = 0, len(nums) - 1

        mid = (r - l) // 2

        while (r - l) >= 0:
            mid = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1



if __name__ == '__main__':
    solution = Solution()

    test.run_test(solution.search, ([-1, 0, 3, 5, 9, 12], 12), 5, '')
    test.run_test(solution.search, ([-1, 0, 3, 5, 9, 12], 2), -1, '')
    test.run_test(solution.search, ([5], 5), 0, '')
    test.run_test(solution.search, ([2, 5], 5), 1, '')


