### Lev.0 한 번만 등장한 문자

# 문자열 s가 매개변수로 주어집니다.
# s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

### 첫번째 풀이: 중복을 없애는 방법으로 set함수를 적극 사용중이다. 효율면에서 훨씬 좋은 것 같다.
def solution(s):
    ans = ''
    for i in set(s):
        if list(s).count(i) == 1:
            ans += i
    return ''.join(sorted(ans))
  
### 두번째 풀이: 위 코드를 간결하게.
def solution(s):
    answer = "".join(sorted([i for i in set(s) if s.count(i) == 1]))
    return answer
