### Lev.0 팩토리얼

# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다.
# 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다.
# 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
# i! ≤ n
# 
# 제한사항
# 0 < n ≤ 3,628,800

### 제한사항을 활용하여 반복문의 범위를 설정했다. 2점!!
def solution(n):
    i = 1
    for j in range(1, 12):
        i *= j
        if i > n: return j-1

### factorial 함수를 사용하는 간단한 방법도 있다.
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
