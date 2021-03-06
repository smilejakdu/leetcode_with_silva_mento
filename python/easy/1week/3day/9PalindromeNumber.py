''':arg

Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''

''':arg
answer1
'''


def isPalindrome(x):
    number = str(x)
    if 0 > x:
        return False
    reverse_number = number[::-1]
    if number == reverse_number:
        return True

    return False


''':arg
answer2
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]


''':arg
answer3
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_list = str(x)[::-1]

        if string_list == str(x):
            return True
        else:
            return False
