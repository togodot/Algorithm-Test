### Lev.0 수열과 구간 쿼리 1

# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

### 배열 안의 두 원소를 각각 s,e 변수에 저장한 후 for문을 진행했다. 2점
def solution(arr, queries):
    for query in queries:
        s, e = query
        for i in range(s, e+1):
            arr[i] += 1
    return arr
