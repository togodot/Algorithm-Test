### Lev.0 369게임

# 머쓱이는 친구들과 369게임을 하고 있습니다. 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다.
# 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

### 문자열로 바꿔 3,6,9를 단순 count 합하였다. 2점!
def solution(order):
    return str(order).count('3') + str(order).count('6') + str(order).count('9')

### 똑같이 문자열 count지만 각각을 직접 더하지 않고, lambda로 해결
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
