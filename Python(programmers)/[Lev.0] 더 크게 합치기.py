### Lev.0 더 크게 합치기

# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
# 
# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

### 두 정수를 이어붙이기 위해 str형태로 바꾼 후 각 경우에 대해 if문으로 비교했다. 1점
def solution(a, b):
    a,b = str(a), str(b)
    return int(a+b) if int(a+b) >= int(b+a) else int(b+a)

### a,b를 str함수로 변환/연산하지 않고 f스트링만으로 해결한 점, if문으로 각 경우를 비교하지 않고 max함수로 최댓값을 바로 출력한 점. >> 효율적인 코드 작성에 대해 매번 고민해볼 필요가 있다.
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
