### Lev.1 소수 찾기

# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다. (1은 소수가 아닙니다.)
# 
# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

### 소수 판별을 위해, 각 숫자의 제곱근까지의 수를 나누어 약수를 찾는 함수를 primenumber로 생성한 후 확인했다. 8점!
def primenumber(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return 0
    return 1

def solution(n):
    answer = 0
    for i in range(2, n+1):
        answer += primenumber(i)
    return answer

### 에라토스테네스의 체를 적절하게 활용했다.
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
