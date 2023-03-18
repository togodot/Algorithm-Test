### Lev.1 두 정수 사이의 합

# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

### 첫 번째 풀이: for문을 사용해서 단순하게 더했다.
def solution(a, b):
    answer = sum(i for i in range(min(a,b), max(a,b)+1))
    return answer

### 두 번째 풀이: for문을 사용하지 않아도 결과가 같았다.
def solution(a, b):
    answer = sum(range(min(a,b), max(a,b)+1))
    return answer

### 세 번째 풀이: 성능 개선을 위해 for문을 사용하지 않고 가우스의 공식을 이용했다.
def solution(a, b):
    answer = (a+b) * (max(a,b) - min(a,b) + 1) // 2
    return answer
