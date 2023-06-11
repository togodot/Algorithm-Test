### Lev.0 문자열 정수의 합

# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

### map함수에 str 형태 값을 그대로 넣으면 한 자리씩 인식된다. 1점
def solution(num_str):
    return sum(map(int, num_str))
