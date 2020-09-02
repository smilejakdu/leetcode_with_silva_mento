'''
Q . 1
"화이팅" 을 출력하세요 .
'''


def question_one():
    return


''':arg
Q . 2
num 과 num 을 받고 더한값을 출력하세요
'''


def question_two():
    return


''':arg
Q . 3
input :  "심리학이 이렇게 쓸모 있을 줄이야"  
output : "심리학이 이렇게 쓸모 없을 줄이야"
'''


def question_three():
    return


''':arg
Q . 4
객체지향이 무엇인가요 ??
'''

''':arg
Q . 5
오름차순으로 정렬해주세요 
input : [ 2 , 5 , 9 , 3 , 6 ]
output : [2 , 3 , 5 , 6 , 9]
'''


def question_five():
    return


''':arg
Q . 6
1부터 100까지의 숫자가 들어있는 배열이 들어있습니다.
2의 배수만 출력해주세요.
'''

def question_six():

    return

''':arg

변수에 저장할 수 있는 값(value)은 string 뿐만이 아닙니다.
숫자 값도 저장 할 수 있습니다.

age = 3
print(age) ## 3 출력

숫자를 변수에 저장할 때 조심해야 할 점은 string 과 다르게 따옴표를 사용하면 안된다는 점입니다.
만일 따옴표를 사용하면 숫자 가 아니라 string 즉 문자열로 인식이 되게 됩니다.

age = "3"
year = age + 1

print(year)

위에 코드를 실행 시키면 다음과 같은 에러가 발생됩니다:

Traceback (most recent call last):   
    File "python", line 2, in <module> 
TypeError: must be str, not int

자 왜 에러가 났는지 한번 생각해봅니다. 






생각해 보셨나요 ??? 
age 라는 변수는 string 이고 거기에 int 1 이 더해지기 때문에 에러가 발생합니다.

자 이제 스스로 어떻게 할지 해결해봅니다.








해결해 보셨나요??

age = 23
year = age + 1

print(next_year) # 24

'''
