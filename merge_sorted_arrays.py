# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Task: Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# Nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Algorithm runs in O(m + n) time

import my_utils.testing as tst


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_p = m - 1
        nums2_p = n - 1
        counter = 1
        while nums1_p >= 0 and nums2_p >= 0:
            if nums1[nums1_p] > nums2[nums2_p]:
                nums1[m + n - counter] = nums1[nums1_p]
                nums1_p -= 1
            else:
                nums1[m + n - counter] = nums2[nums2_p]
                nums2_p -= 1
            counter += 1
        while nums2_p >= 0:
            nums1[m + n - counter] = nums2[nums2_p]
            nums2_p -= 1
            counter += 1

        return nums1


if __name__ == '__main__':
    solution = Solution()

    tst.run_test(solution.merge, ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6], '')
    tst.run_test(solution.merge, ([1], 1, [], 0), [1], '')
    tst.run_test(solution.merge, ([0], 0, [1], 1), [1], '')
    tst.run_test(solution.merge, ([2, 0], 1, [1], 1), [1, 2], '')
    tst.run_test(solution.merge, ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3), [1, 2, 3, 4, 5, 6], '')
    tst.run_test(solution.merge, ([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5], '')
