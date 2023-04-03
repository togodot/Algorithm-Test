### Lev.0 컨트롤 제트

# 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다.
# 문자열에 있는 숫자를 차례대로 더하려고 합니다.
# 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
# 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

### eval 함수를 사용했다. Z를 '*0'으로 변환한 후 모든 값을 더했다. 1점
def solution(s):
    return eval(s.replace(' Z', '*0').replace(' ','+'))

### eval 함수 없이, Z를 '-이전값'으로 변환하여 더하는 방법이다.
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer
