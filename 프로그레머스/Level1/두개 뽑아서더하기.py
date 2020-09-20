''':arg
정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서
만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.
numbers   	result
[2,1,3,4,1]	[2,3,4,5,6,7]
[5,0,2,7]	[2,5,7,9,12]
'''
# numbers = [2, 1, 3, 4, 1]
numbers = [5, 0, 2, 7]


def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for r in range(i + 1, len(numbers)):
            if not numbers[i] + numbers[r] in answer:
                answer.append(numbers[i] + numbers[r])
    answer.sort()
    return answer


''':arg
다른사람 풀이
'''


def solution(numbers): return sorted(
    {numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i > j})


print(solution(numbers))
