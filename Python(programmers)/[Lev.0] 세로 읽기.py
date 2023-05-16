### Lev.0 세로 읽기

# 문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

### 결국 간격의 문제이기 때문에 c번째 글자를 시작으로 m개 글자 간격으로 my_string을 슬라이싱했다. 1점
def solution(my_string, m, c):
    return my_string[c-1::m]
