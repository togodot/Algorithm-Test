### Lev.0 정사각형으로 만들기

# 이차원 정수 배열 arr이 매개변수로 주어집니다.
# arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

### 최대한 append, extend를 안 쓰려고 했는데 결국 extend를 썼다 ㅠ 여러 개의 0을 추가하기 위함. 2점
def solution(arr):
    r, c = len(arr), len(arr[0])
    if r > c:
        [a.extend([0]*(r-c)) for a in arr]
    if r < c:
        arr += [[0]*c]*(c-r)

    return arr
