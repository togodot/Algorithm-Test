### Lev.1 자릿수 더하기

# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

def solution(x):
    n = 0
    for i in range(len(str(x))):
        n += int(str(x)[i])
    answer = n
    return answer

### (2023.04.01) map함수로 더 간단한 코드 작성이 가능하다!
def solution(n):
    return sum(list(map(int, str(n))))
