### Lev.0 qr code

# 두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

### 단순한 접근. enumerate로 인덱스와 값을 for문으로 확인했다. 1점
def solution(q, r, code):
    return ''.join(s for i, s in enumerate(code) if i%q == r)

### 문자열 슬라이싱을 잘 활용한 방법. 이렇게 풀고 싶었다,,,
def solution(q, r, code):
    return code[r::q]
