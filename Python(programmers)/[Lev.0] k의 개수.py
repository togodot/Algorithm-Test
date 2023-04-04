### Lev.0 k의 개수

# 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다.
# 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

### 모든 수를 하나의 문자열로 만든 후 count
def solution(i, j, k):
    arr = ''
    for a in range(i, j+1): arr += str(a)
    return arr.count(str(k))

### 범위 내 숫자들을 for문으로 돌리며 매번 count하는 방법
def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer

### 위 방법을 lambda 함수로.
def solution(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))
