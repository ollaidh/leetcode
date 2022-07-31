# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        values = set()
        for num in nums:
            if num in values:
                return True
            values.add(num)
        return False
    