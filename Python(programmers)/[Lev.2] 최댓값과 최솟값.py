### Lev.2 최댓값과 최솟값

# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
# 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

### map함수를 사용해서 int, str 형태로 바꿔가며 확인했다.
def solution(s):
    sl = list(map(int, s.split(' ')))
    return ' '.join(map(str, (min(sl),max(sl))))

### f스트링을 적극 활용하자!!!
def solution(s):
    sl = list(map(int, s.split(' ')))
    return f'{min(sl)} {max(sl)}'
