'''

입력조건
- 첫째 줄에 공간의 크기를 나타내는 N 이 주어진다. ( 1 <= N <= 100)
- 둘째 줄에 여행가 A 가 이동할 계획서 내용이 주어진다. ( 1 <= 이동횟수 <= 100)

출력 조건
- 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 ( x , Y ) 를 공백으로 구분하여 출력한다.

입력 예시
5
R R R U D D

출력 예시
3 4
'''

n = 5
plans = ["R", "R", "R", "U", "D", "D"]
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)

