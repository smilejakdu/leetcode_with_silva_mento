''':arg
2016년 1월 1일은 금요일입니다.
2016년 a월 b일은 무슨 요일일까요?
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

제한 조건
- 2016년은 윤년입니다.
- 2016년 a월 b일은 실제로 있는 날입니다. ( 13월 26일이나 2월 45일 같은 날짜는 주어지지 않습니다. )

입출력 예

a  b  result
5  24  "TUE"
'''

import datetime

a = 5
b = 24


def solution(a, b):
    day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAY']
    answer = day_list[datetime.date(2016, a, b).weekday()]
    return answer


print(solution(a, b))
