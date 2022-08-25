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
    insert_def = Solution()
    if insert_def.searchInsert([1, 3, 5, 6], 5) != 2:
        print('WRONG case ([1, 3, 5, 6], 5) ----', 'Expected: 2', 'Got:', insert_def.searchInsert([1, 3, 5, 6], 5))
    else:
        print('ok case ([1, 3, 5, 6], 5) ----', 'Expected: 2', 'Got:', insert_def.searchInsert([1, 3, 5, 6], 5))

    if insert_def.searchInsert([1, 3, 5, 6], 2) != 1:
        print('WRONG case ([1, 3, 5, 6], 2) ----', 'Expected: 1', 'Got:', insert_def.searchInsert([1, 3, 5, 6], 2))
    else:
        print('ok case ([1, 3, 5, 6], 2) ----', 'Expected: 1', 'Got:', insert_def.searchInsert([1, 3, 5, 6], 2))

    if insert_def.searchInsert([1, 3], 0) != 0:
        print('WRONG case ([1, 3], 0) ----', 'Expected: 0', 'Got:', insert_def.searchInsert([1, 3], 0))
    else:
        print('ok case ([1, 3], 0) ----', 'Expected: 0', 'Got:', insert_def.searchInsert([1, 3], 0))

    if insert_def.searchInsert([1, 3], 1) != 0:
        print('WRONG case ([1, 3], 1) ----', 'Expected: 0', 'Got:', insert_def.searchInsert([1, 3], 1))
    else:
        print('ok case ([1, 3], 1) ----', 'Expected: 0', 'Got:', insert_def.searchInsert([1, 3], 1))

    if insert_def.searchInsert([1,4,6,7,8,9], 6) != 2:
        print('WRONG case ([1,4,6,7,8,9], 6) ----', 'Expected: 2', 'Got:', insert_def.searchInsert([1,4,6,7,8,9], 6))
    else:
        print('ok case ([1,4,6,7,8,9], 6) ----', 'Expected: 2', 'Got:', insert_def.searchInsert([1,4,6,7,8,9], 6))

    if insert_def.searchInsert([1,2,4,6,7], 3) != 2:
        print('WRONG case ([1,2,4,6,7], 3) ----', 'Expected: 2', 'Got:', insert_def.searchInsert([1,2,4,6,7], 3))
    else:
        print('ok case ([1,2,4,6,7], 3) ----', 'Expected: 2', 'Got:', insert_def.searchInsert([1,2,4,6,7], 3))

    if insert_def.searchInsert([2,3,5,6,9], 7) != 4:
        print('WRONG case ([2,3,5,6,9], 7) ----', 'Expected: 4', 'Got:', insert_def.searchInsert([2,3,5,6,9], 7))
    else:
        print('ok case ([2,3,5,6,9], 7) ----', 'Expected: 4', 'Got:', insert_def.searchInsert([2,3,5,6,9], 7))