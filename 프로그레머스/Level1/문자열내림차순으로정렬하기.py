''':arg
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수,
solution을 완성해주세요.

s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

str은 길이 1 이상인 문자열입니다.

s	        return
Zbcdefg     gfedcbZ

'''

s = 'Zbcdefg'


def solution(s):
    upper_list, lower_list = sorted([i for i in s if i.isupper()], reverse=True), \
                             sorted([i for i in s if i.islower()], reverse=True)

    return ''.join(lower_list + upper_list)


print(solution(s))


# 다른사람 풀이 2


def solution(s):
    list_s = list(s)
    list_s.sort(reverse=True)
    return ''.join(list_s)
