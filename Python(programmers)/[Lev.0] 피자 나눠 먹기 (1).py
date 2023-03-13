### Lev.0 피자 나눠 먹기 (1)
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다.
# 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

def solution(n):
    return n//7 if n%7 == 0 else n//7 + 1


### 한 번 더 생각해보면 이렇게 단순하고 확실한 코드가 만들어진다.!
def solution(n):
    return (n - 1) // 7 + 1
