''':arg
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수,
solution을 완성하세요. 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.

입출력 예
n	return
3	수박수
4	수박수박
'''

n = 3


def solution(n):
    answer = ''
    su = '수'
    park = '박'

    for i in range(1, n + 1):
        if i % 2 == 1:
            answer += su
        elif i % 2 == 0:
            answer += park

    return answer


print(solution(n))


# 다른풀이

def water_melon(n):
    s = "수박" * n
    return s[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3))
print("n이 4인 경우: " + water_melon(4))


# 다른풀이 2

def solution(n):
    return "".join(["수박"[i % 2] for i in range(n)])
