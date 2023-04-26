### Lev.0 그림 확대

# 직사각형 형태의 그림 파일이 있고, 이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다.
# 이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때, 이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
# 
# 제한사항
# 1 ≤ picture의 길이 ≤ 20
# 1 ≤ picture의 원소의 길이 ≤ 20
# 모든 picture의 원소의 길이는 같습니다.
# picture의 원소는 '.'과 'x'로 이루어져 있습니다.
# 1 ≤ k ≤ 10

### 제한사항의 범위가 길지 않아 이중 for문으로 해결
def solution(picture, k):
    arr = [''.join(x*k for x in s) for s in picture]
    return [i for i in arr for j in range(k)]
