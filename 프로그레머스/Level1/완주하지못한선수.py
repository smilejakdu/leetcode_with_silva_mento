''':arg

https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

participant = ["leo", "kiki", "eden"]
completion  = ["eden, "kiki]
return = "leo"

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
return = "vinko"


participant =["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
return =  "mislav"
'''

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


# return = "vinko"


def solution(participant, completion):
    answer = ''

    if len(completion) == 0:
        return answer.join(participant)

    for par in participant:
        if par in completion:
            participant.remove(par)
            completion.remove(par)
            return solution(participant, completion)


print(solution(participant, completion))


# 다른사람 풀이

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[len(participant) - 1]

# 다른 사람 풀이 2


def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


# 다른사람 풀이 3

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
