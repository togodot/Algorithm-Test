### Lev.0 2의 영역

# 정수 배열 arr가 주어집니다. 배열 안의 모든 2를 포함하는 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

### 앞에서부터 2를 찾고 뒤에서 부터 2를 찾은 후 슬라이싱. 8점!?
def solution(arr):
    return [-1] if 2 not in arr else arr[arr.index(2):len(arr)-arr[::-1].index(2)]
