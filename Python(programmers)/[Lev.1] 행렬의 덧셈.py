### Lev.1 행렬의 덧셈

# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

### List Comprehension으로 2중 for문으로 풀이했다.
def solution(arr1, arr2):
    return [[arr1[i][j]+arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

### zip을 사용한 풀이도 있었다.
### zip 함수 => 길이가 같은 두개 이상의 자료형에 대하여 동일한 위치의 자료끼리 튜플 형태로 묶어주는 역할을 수행.
def solution(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer
