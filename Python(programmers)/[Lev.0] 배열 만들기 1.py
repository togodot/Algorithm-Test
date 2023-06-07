### Lev.0 배열 만들기 1

# 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

### 문제에서 주어진 흐름 그대로 코딩. 1점
def solution(n, k):
    for i in range(1,1000000):
        if i*k > n:
            return [j*k for j in range(1,i)]

### range함수에 시작,끝,간격 인자를 설정할 수 있다는 점을 활용하는 방법.
def solution(n, k):
    return [i for i in range(k,n+1,k)]
