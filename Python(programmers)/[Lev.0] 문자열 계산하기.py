### Lev.0 문자열 계산하기

# my_string은 "3 + 5"처럼 문자열로 된 수식입니다.
# 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

### 파이썬 내장함수인 eval을 사용해 간단하게 풀었다. 4점!!
def solution(my_string):
    return eval(my_string)

## 하지만 eval 함수는 보안취약성을 가지고 있기 때문에 실무에서는 사용하지 않는다고 한다. >> 수식을 음수값을 더하는(+) 형태로 변환하여 계산한다.
def solution(my_string):
    return sum(list(map(int, my_string.replace(' - ', ' + -').split(' + '))))
