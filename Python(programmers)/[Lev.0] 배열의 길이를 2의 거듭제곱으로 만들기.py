### Lev.0 배열의 길이를 2의 거듭제곱으로 만들기

# 정수 배열 arr이 매개변수로 주어집니다.
# arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다.
# arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.

### 2의 거듭제곱임을 확인하는데, 제한사항으로 2의 10승까지의 수가 범위라 for문으로 확인했다. 10점!
def solution(arr):
    for i in range(10):
        if len(arr) == 2**i:
            return arr
        if 2**i < len(arr) < 2**(i+1):
            arr += [0] * (2**(i+1) - len(arr))
            return arr
