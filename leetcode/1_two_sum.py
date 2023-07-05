# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

import collections

class Solution(object):
    def twoSum(self, nums, target):
        index_list = []
        counter = 0
        print("INPUT:", nums)
        for i in range(len(nums)):
            counter += 1
            for j in range(len(nums)):
                if nums[j] == target - nums[i] and i != j:
                    index_list.append(i)
                    index_list.append(j)
                    return index_list
        # nums_dict = {}
        # index = 0
        # for number in nums:
        #     if number not in nums_dict:
        #         nums_dict[number] = [index, 1]
        #     index += 1
        # ord_nums_dict = dict(sorted(nums_dict.items()))
        # print(ord_nums_dict)
        #
        # index_list = []
        # for obj in ord_nums_dict:
        #     if ((target-int(obj)) in ord_nums_dict) and (ord_nums_dict[obj] != ord_nums_dict[target-int(obj)]):
        #         index_list.append(ord_nums_dict[obj])
        #         index_list.append(ord_nums_dict[target-int(obj)])
        #         index_list.sort()
        #         return index_list


if __name__ == '__main__':
    hahaha = Solution()
    print(hahaha.twoSum([3,3], 6))
    print(hahaha.twoSum([2,7,11,15], 9))