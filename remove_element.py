# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
# Have the result be placed in the first part of the array nums.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.

# HOW TO SOLVE THIS:
# Two pointers: left (moves through every element of the list) and right (indicates
# the last element of the list, which is not equal to val). If left pointer is equal to val, we swap it with the
# last element of the list, which is not equal to val (aka right pointer). So we have all non-equal to val values
# at the beginning of the list and all val-equal values at the end of the list


class Solution(object):
    def removeElement(self, nums, val):
        rp = len(nums) - 1
        lp = 0
        while lp <= rp:
            if nums[rp] == val:
                rp -= 1
            else:
                if nums[lp] == val:
                    nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
        return lp


if __name__ == '__main__':
    remover = Solution()
    print(remover.removeElement([3, 2, 2, 3], 3))
    print(remover.removeElement([0, 1, 2, 2, 3, 0, 4, 2, 2, 2, 2], 2))
    print(remover.removeElement([2], 3))
    print(remover.removeElement([1], 1))