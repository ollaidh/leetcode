# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.

# SOLUTION:
# Place unique values instead of duplicates
# Two pointers: wt (write to) - duplicate instead of which we write the unique value,
# increases if we wrote smth to the previous
# ww (write what) - points on unique value, increases every step

class Solution(object):
    def removeDuplicates(self, nums):
        wt, ww = 1, 1
        while ww < len(nums):
            if nums[ww] != nums[ww - 1]:
                nums[wt] = nums[ww]
                wt += 1
            ww += 1
        return wt


if __name__ == '__main__':
    remover = Solution()
    print(remover.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(remover.removeDuplicates([1, 1, 2]))
