### Lev.0 대문자와 소문자

# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

### isupper()로 단순 확인
def solution(my_string):
    return ''.join(s.lower() if s.isupper() == True else s.upper() for s in my_string)

### 대소문자를 바꿔주는 메서드 swapcase()를 활용하는 간단한 방법!
def solution(my_string):
    return my_string.swapcase()
