### Lev.0 A로 B 만들기

# 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def solution(before, after):
    b = sorted(list(before))
    a = sorted(list(after))
    return 1 if b == a else 0

### 문자열을 list에 담은 후 정렬했는데, 다시 보니 list에 담을 필요 없이 문자열을 sorted하면 알아서 리스트에 저장되었다.. >> list로 묶을 필요가 없었던 것!
def solution(before, after):
    b = sorted(before)
    a = sorted(after)
    return 1 if b == a else 0

### 그래서 이렇게 한줄로도 요약이 가능하다.
def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0
