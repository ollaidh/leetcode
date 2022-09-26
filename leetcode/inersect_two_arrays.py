# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and the result may be returned in any order.

import my_utils.testing as tst


class Solution(object):
    def intersection(self, nums1, nums2):
        testset = set(nums1)
        intersected = set()
        for num in nums2:
            if num in testset:
                intersected.add(num)
        return list(intersected)


if __name__ == '__main__':
    solution = Solution()
    tst.run_test(solution.intersection, ([1, 2, 2, 1], [2, 2]), [2], '')
    tst.run_test(solution.intersection, ([4, 9, 5], [9, 4, 9, 8, 4]), [9, 4], '')
    tst.run_test(solution.intersection, ([], []), [], '')
