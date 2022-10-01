# Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must appear
# as many times as it shows in both arrays, return the result in any order.

import my_utils.testing as tst


class Solution(object):
    def intersect(self, nums1, nums2):
        nums1_dict = {}
        nums2_dict = {}
        intersected = []

        for num in nums1:
            nums1_dict[num] = nums1_dict.get(num, 0) + 1

        for num in nums2:
            nums2_dict[num] = nums2_dict.get(num, 0) + 1

        for obj in nums1_dict:
            if obj in nums2_dict:
                for i in range(min(nums1_dict[obj], nums2_dict[obj])):
                    intersected.append(obj)

        return intersected


if __name__ == '__main__':
    solution = Solution()
    tst.run_test(solution.intersect, ([1, 2, 2, 1], [2, 2]), [2, 2], '')
    tst.run_test(solution.intersect, ([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9], '')
    tst.run_test(solution.intersect, ([4, 9, 5], []), [], '')
    tst.run_test(solution.intersect, ([4, 4, 4], [2, 2, 2, 2]), [], '')
    tst.run_test(solution.intersect, ([5, 8, 9, 1], [8, 9, 5, 1]), [5, 8, 9, 1])
    tst.run_test(solution.intersect, ([1, 2, 2, 1], [2]), [2])




