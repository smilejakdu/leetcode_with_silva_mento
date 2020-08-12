''':arg
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

''':arg
딱히 좋은 문제라고 생각이 들지 않았다 . 밑의 풀이를 보면 파라미터 n 을 사용하지 않아도 코드가 정상적으로 돌아간다.
'''


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    while len(nums1) != m:
        nums1.pop()
    for i in nums2:
        nums1.append(i)
    nums1.sort()

''':arg
원래라면 num2 도 이렇게 filter 를 해줘야 하지 않을까 ?? 라는 생각을 했다. 
그리고 저는 for 문을 자주 사용하는데 때에 따라서 while 문을 사용하는것이 더 효율적이라는 것도 배웠다 .

'''
def merge(nums1, m, nums2, n):
    while len(nums1) != m:
        nums1.pop()
    while len(nums2) != n:
        nums2.popO()
    for i in nums2:
        nums1.append(i)
    nums1.sort()
    return
