''':arg
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

''':arg
answer1
'''

# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     for n in nums:
#         if nums.count(n) == 1:
#             return n


''':arg
answer2
'''

nums = [2, 2, 1]


def singleNumber(nums):
    nums.sort()

    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]

    return nums[-1]


''':arg
answer3
'''


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()
