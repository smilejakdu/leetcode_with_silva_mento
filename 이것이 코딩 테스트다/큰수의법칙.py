''':arg
순서대로 2 , 4 , 5 , 4 , 6 으로 이루어진 배열이 있을 때 M 이 8이고 , K 가 3이라고 가정하자.
이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는
6 + 6 + 6 + 5 + 6 + 6 + 6 + 6 인 46 이 된다.

n 은 배열의 크기
m 은 숫자가 더해지는 횟수
k 는 연속해서 더 할 수 있는 횟수
'''

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
data.sort()  # 입력 받은 수들 정렬하기
first = data[n - 1]  # 가장 큰수
second = data[n - 2]  # 두 번째로 큰수
result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k 번 더하기
        if m == 0:
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m 이 0 이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)
