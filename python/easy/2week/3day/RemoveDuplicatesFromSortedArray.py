''':arg
Given a sorted array nums,
remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
이거는 제가 풀지 않았고 , 괜찮은 풀이가 있어서 적었습니다.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        for num in nums[::-1]:
            if nums.count(num) > 1:
                nums.remove(num)
        return len(nums)


''':arg
answer 2 
이거는 조금 문제가 있는게 중복된 숫자가 연속으로 나올때는 상관이 없겠지만 
만약에 중복된 수가 연속으로 나오지 않을경우 문제가 생긴다.
'''


class Solution:
    def removeDuplicates(self, nums):

        index = 1

        while index < len(nums):
            if nums[index] == nums[index - 1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)
