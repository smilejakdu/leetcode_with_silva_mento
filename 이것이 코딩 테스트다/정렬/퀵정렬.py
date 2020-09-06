''':arg
퀵 정렬은 지금까지 배운 정렬 알고리즘 중에 가장 많이 사용되는 알고리즘이다.
퀵정렬은 어떻게 구성되어있길래 말이 퀵정렬일까 ??

" 기중 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까 ?? "

하나의 리스트를 피벗(pivot) 을 기준으로 두 개의 비균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음 ,
두 개의 정렬된 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법이다.

- 분할 정복 방법
1. 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음 , 결과를 모아서 원래의 문제를 해결하는 전략이다.
2. 분할 정복 방법은 대개 순환 호출을 이용하여 구현한다.

- 과정설명

1. 리스트 안에 있는 한 요소를 선택한다. 이렇게 고른 원소를 피벗이라고 한다.
2. 피벗을 기준으로 피벗보다 작은 요소들은 모두 피벗의 왼쪽으로 옮겨지고
 피벗보다 큰 요소들은 모두 피벗의 오른쪽으로 옮겨진다.

3. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.

'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 , 전체 리스트를 반환

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
