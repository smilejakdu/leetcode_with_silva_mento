''':arg

배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.


 arr	              answer
[1,1,3,3,0,1,1]	  [1,3,0,1]
[4,4,4,3,3]	      [4,3]
'''
arr = [1, 1, 3, 3, 0, 1, 1]


def solution(arr):
    answer = []

    for i in range(0, len(arr)):
        answer.append(arr[i])
        if not i == 0 and arr[i - 1] == arr[i]:
            answer.pop()

    return answer


print(solution(arr))


# 다른사람 코드


# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(no_continuous("133303"))
