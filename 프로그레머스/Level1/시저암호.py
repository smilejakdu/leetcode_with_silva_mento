''':arg
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다.
z는 1만큼 밀면 a가 됩니다.
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건

- 공백은 아무리 밀어도 공백입니다.
- s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
- s의 길이는 8000이하입니다.
- n은 1 이상, 25이하인 자연수입니다.

입출력 예

s	    n	result
AB	    1	BC
z	    1	a
a B z	4	e F d
'''

s = "AB"
n = 1


def solution(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    result = ""
    for c in s:
        if c == ' ':
            replace = ' '
        else:
            replace = c.lower()
            index = (alphabet.index(replace) + n) % 26
            replace = alphabet[index]
            if c.isupper():
                replace = replace.upper()
        result += replace

    return result


print(solution(s, n))


# 다른 사람 풀이 2

def solution(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    for i in s:
        if i is " ":
            result.append(" ")
        elif i.islower():
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])

    return "".join(result)


# 다른 사람 풀이 3
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + solution("a B z", 4))
