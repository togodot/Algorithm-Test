### Lev.0 겹치는 선분의 길이

# 선분 3개가 평행하게 놓여 있습니다.
# 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때,
# 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.
# lines가 [[0, 2], [-3, -1], [-2, 1]]일 때, 선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

### range로 각 구간을 정수로 나열한 후 set함수로 교집합을 찾는 방식을 사용했다. set함수의 연산기호에 대해 공부할 수 있었다. 교집합(&), 합집합(|), 차집합(-)
def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))

### 최초로 세 구간을 각 변수에 담는 과정 대신 각 구간 set들을 리스트 안에 담으면 코드가 좀더 간결해진다. >> 최종제출, 7점
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
