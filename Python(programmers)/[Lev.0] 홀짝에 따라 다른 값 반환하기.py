### Lev.0 홀짝에 따라 다른 값 반환하기

# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

### 단순하게 각 경우에 따라 조건문으로 결과값을 반환했다. 1점
def solution(n):
    if n%2 != 0:
        return sum(i for i in range(1,n+1,2))
    else:
        return sum(i**2 for i in range(2, n+1, 2))

### if문에서 꼭 ==0을 안해도 된다는 사실..
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])
