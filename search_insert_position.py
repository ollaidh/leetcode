import my_utils.testing as test


class Solution(object):
    def searchInsert(self, nums, target):
        lp, rp = 0, len(nums) // 2

        while lp <= rp:
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            if target == nums[rp]:
                return rp
            if target == nums[lp]:
                return lp

            if lp == rp:
                return rp + 1

            if target > nums[rp]:
                dummy = rp
                rp = rp + (len(nums) - rp) // 2
                lp = dummy
            elif target < nums[rp]:
                rp = lp + (rp - lp) // 2


if __name__ == '__main__':
    solution = Solution()

    test.run_test(solution.searchInsert, ([1, 3, 5, 6], 5), 2, '')
    test.run_test(solution.searchInsert, ([1, 3, 5, 6], 2), 1, '')
    test.run_test(solution.searchInsert, ([1, 3], 0), 0, '')
    test.run_test(solution.searchInsert, ([1, 3], 1), 0, '')
    test.run_test(solution.searchInsert, ([1, 4, 6, 7, 8, 9], 6), 2, '')
    test.run_test(solution.searchInsert, ([1, 2, 4, 6, 7], 3), 2, '')
    test.run_test(solution.searchInsert, ([2, 3, 5, 6, 9], 7), 4, '')
