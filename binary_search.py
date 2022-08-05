# Given an array of integers nums which is sorted in ascending order, and an integer
# target, write a function to search target in nums.\
# If target exists, then return its index.Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


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
    numbers = Solution()

    if numbers.search([-1,0,3,5,9,12], 12) == 5:
        print('[-1,0,3,5,9,12], 12: Test OK')
    else:
        print('[-1,0,3,5,9,12], 12: Test FAILED.   Expected: 5, Got:', numbers.search([-1,0,3,5,9,12], 12))

    if numbers.search([-1,0,3,5,9,12], 2) == -1:
        print('[-1,0,3,5,9,12], 2: Test OK')
    else:
        print('[-1,0,3,5,9,12], 2: Test FAILED.   Expected: -1, Got:', numbers.search([-1,0,3,5,9,12], 2))

    if numbers.search([5], 5) == 0:
        print('[5], 5: Test OK')
    else:
        print('[5], 5: Test FAILED.   Expected: 0, Got:', numbers.search([5], 5))

    if numbers.search([2, 5], 5) == 1:
        print('[2, 5], 5: Test OK')
    else:
        print('[2, 5], 5: Test FAILED.   Expected: 1, Got:', numbers.search([2, 5], 5))

