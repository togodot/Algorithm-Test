### Lev.0 모음 제거

# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

### 특정 문자열을 제거하는 과정을 조건문으로 확인하여 제거했다.
def solution(my_string):
    return ''.join(i for i in my_string if i not in ('a', 'e', 'i', 'o', 'u'))

### 위 코드에서 조건인 모음을 분리하지 않고 한 번에 하는 방법이다.
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
