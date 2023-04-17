### Lev.0 인덱스 바꾸기

# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

### 문자열에서 swap은 되지 않는다. replace의 경우 index로 접근하기 어렵기에, 문자열을 리스트로 바꾼 후 인덱스로 접근할 수 있었다.
def solution(my_string, num1, num2):
    temp = list(my_string)
    temp[num1], temp[num2] = temp[num2], temp[num1]
    return ''.join(temp)
