''':arg
대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

제한사항

문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.

s	        answer

pPoooyY	    true
Pyy	        false
'''

s = "pPoooyY"


def solution(s):
    s = s.lower()
    y_count = 0
    p_count = 0

    for i in s:
        if i == "y":
            y_count += 1
        elif i == "p":
            p_count += 1

    if y_count == p_count:
        return True
    else:
        return False


print(solution(s))


# 다른 풀이
def numPY(s):
    # 함수를 완성하세요
    if (s.upper().count('P') == s.upper().count('Y')):
        return True
    return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numPY("pPoooyY"))
print(numPY("Pyy"))
