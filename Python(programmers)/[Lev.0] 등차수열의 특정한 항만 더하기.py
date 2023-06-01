### Lev.0 등차수열의 특정한 항만 더하기

# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
# 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

### a로 시작하는 d 간격의 배열을 만들기 위해 range함수를 사용했다. 전체 숫자 배열을 먼저 만든 후, 각 항의 bool값을 확인해서 합하는 방식으로 풀이했다. 1점
def solution(a, d, included):
    return sum(n for i, n in enumerate(list(range(a,a+d*len(included),d))) if included[i] == True)

### 숫자 배열을 먼저 만드는 대신, bool 값을 먼저 확인한 후 True인 항의 값을 만들어서 더하는 방식이다. 위 풀이보다 성능이 좀더 빠른 것 같다.
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)
