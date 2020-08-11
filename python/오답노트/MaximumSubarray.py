''':arg
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSubArray(nums):
    maxcurr = nums[0]
    maxglobal = nums[0]
    for i in range(1, len(nums)):
        maxcurr = max(nums[i], maxcurr + nums[i])
        maxglobal = max(maxcurr, maxglobal)
    return maxglobal  # 4


print(maxSubArray(nums))
