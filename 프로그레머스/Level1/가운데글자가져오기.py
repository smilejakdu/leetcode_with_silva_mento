''':arg
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

제한사항
- s는 길이가 1 이상, 100이하인 스트링입니다.

s	     return
abcde	 c
qwer	 we
'''
# s = "abcde"


s = "qwer"


def solution(s):
    if len(s) % 2 == 1:  # 홀수
        mid_len = len(s) // 2
        return s[mid_len]

    elif len(s) % 2 == 0:  # 짝수
        mid_len = len(s) // 2
        mid_len_minus = (len(s) // 2) - 1
        answer = s[mid_len_minus] + s[mid_len]
        return answer


print(solution(s))


# 다른사람 풀이 2

# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.

def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str) - 1) // 2:len(str) // 2 + 1]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))


# 다른 사람 풀이 3

# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def string_middle(str):
    # 함수를 완성하세요
    n = len(str)
    if len(str) % 2 == 1:
        return str[(n // 2)]
    else:
        return str[(n // 2 - 1):(n // 2 + 1)]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
print(string_middle("test"))
