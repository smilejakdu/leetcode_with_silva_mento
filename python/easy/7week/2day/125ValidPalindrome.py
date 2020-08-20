''':arg
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem,
we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''

''':arg
answer1
'''

Input = "A man, a plan, a canal: Panama"


# Input = "race a car"


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    letters = [i.lower() for i in s if i.isalnum()]  # derive a list of all alphanumeric letters, in lower-case
    m = max(len(letters) // 2, 1)
    return letters[:m] == letters[-m:][::-1]


print(isPalindrome(Input))

''':arg
answer2
isalnum(): 라는것은 모든 문자열이 string 인지 int 형인지 확인을 한다.
모두 string 이면 true 
마찬가지로 모두 int 이면 true 이다.
반면에 string 과 int 가 섞여있으면 False 이다.
'''


def isPalindrome(string):
    li = []
    for i in string.lower():
        if i.isalnum():
            li.append(i)

    if li == li[::-1]:
        return True

    else:
        return False


print(isPalindrome(Input))

''':arg
answer3
'''


def isPalindrome(string):
    filtered_chars = filter(lambda ch: ch.isalnum(), string)
    lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

    filtered_chars_list = list(lowercase_filtered_chars)
    reversed_chars_list = filtered_chars_list[::-1]

    return filtered_chars_list == reversed_chars_list


print(isPalindrome(Input))
