''':arg

- 첫째 줄에 정수 N 이 주어진다 1 부터 1,000,000 까지이다.
- 둘째 줄에는 공백으로 구분하여 N 개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하 이다.
- 셋째 줄에는 정수 M 이 주어진다 ( 1 =< M =< 1000,000)
- 넷째 줄에는 공백으로 구분하여 M 개의 정수가 주어진다. 이때 정수는 1보다 크고 10억 이하이다.

출력조건

- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 , yes 없으면 no 를 출력한다.

입력 예시
5
8 3 7 9
3
5 7 9

출력 예시
no yes yes
'''


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            start = mid + 1
        return None


n = 5
array = [8, 3, 7, 9, 2]
array.sort()

m = 3
x = [5, 7, 9]

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
