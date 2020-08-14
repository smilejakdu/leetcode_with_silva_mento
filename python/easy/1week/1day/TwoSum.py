''':arg
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        for n1 in range(0, len(nums)):
            for n2 in range(1, len(nums)):
                if nums[n1] + nums[n2] == target and n1 != n2:
                    return [n1, n2]


class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        for index, item in enumerate(nums):
            if (target - item) in lookup:
                return [lookup[target - item], index]
            else:
                lookup[item] = index


