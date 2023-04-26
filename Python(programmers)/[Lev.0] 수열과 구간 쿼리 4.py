### Lev.0 수열과 구간 쿼리 4

# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

### 첫 번째 풀이. 리스트 인덱싱으로 비교했다. 2점
def solution(arr, queries):
    for s in queries:
        for i in range(s[0], s[1]+1):
            if i%s[2] == 0:
                arr[i] += 1
    return arr

### 같은 코드를 리스트 인덱싱 대신 변수에 저장하여 풀이. 확실히 더 빠르다.
def solution(arr, queries):
    for query in queries:
        s, e, k = query
        for i in range(s, e+1):
            if i%k == 0:
                arr[i] += 1
    return arr
