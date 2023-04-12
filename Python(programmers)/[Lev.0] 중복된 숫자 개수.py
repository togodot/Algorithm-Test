### Lev.0 중복된 숫자 개수

# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

### count함수에 대해서 제대로 알지 못했다. 문자열에만 적용되는 줄 알고 모든 배열과 정수를 문자열로 변환 후 count하였다.
def solution(array, n):
    return list(map(str, array)).count(str(n))

### 숫자로 이루어진 배열에도 바로 count함수가 적용된다.
def solution(array, n):
    return array.count(n)
