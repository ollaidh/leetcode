import my_utils.testing as tst


class Solution(object):
    def moveZeroes(self, nums):
        if not nums:
            return []

        zero = 0
        notzero = 0

        while nums[zero] != 0:
            zero += 1
            notzero += 1
            if zero == len(nums):
                return nums

        while True:
            while nums[zero] != 0:
                zero += 1
                if zero == len(nums):
                    return nums
            while nums[notzero] == 0:
                notzero += 1
                if notzero == len(nums):
                    return nums

            nums[zero], nums[notzero] = nums[notzero], nums[zero]


if __name__ == '__main__':
    solution = Solution()

    tst.run_test(solution.moveZeroes, ([0, 1, 0, 3, 12], ), [1, 3, 12, 0, 0], '')
    tst.run_test(solution.moveZeroes, ([0], ), [0], '')
    tst.run_test(solution.moveZeroes, ([], ), [], '')
    tst.run_test(solution.moveZeroes, ([1, 1, 2, 3], ), [1, 1, 2, 3], '')
    tst.run_test(solution.moveZeroes, ([1, 0],), [1, 0], '')
    tst.run_test(solution.moveZeroes, ([1, 0, 0],), [1, 0, 0], '')
    tst.run_test(solution.moveZeroes, ([1, 0, 1],), [1, 1, 0], '')
    tst.run_test(solution.moveZeroes, ([1, 0, 1, 0, 3, 12],), [1, 1, 3, 12, 0, 0], '')
    tst.run_test(solution.moveZeroes, ([1, 1, 1, 0, 3, 12],), [1, 1, 1, 3, 12, 0], '')