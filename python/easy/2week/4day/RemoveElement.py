''':arg
Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for n in nums[::-1]:
            if val == n:
                nums.remove(n)

        return len(nums)


''':arg
answer2
사실 위의 풀이와 같지만 comprehension 을 사용했다는것에 차이가 있다.
그리고 위에서는 기존에 있는 list 에서 빼는 방식이라면 ,
밑에 방식은 list 를 다시 채워간다.
'''


def removeElement(nums, val):
    nums = [nums[a] for a in range(len(nums)) if nums[a] != val]
    return len(nums)


''':arg
answer3

while 문으로 반복문을 돌린다 
만약에 nums 라는 리스트에 val 이라는 요소가 있다면 while 문을 타게 된다.
'''


def removeElement(nums, val):
    while val in nums:
        nums.pop(nums.index(val))
    return (len(nums))
