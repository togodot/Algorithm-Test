### Lev.0 최댓값 만들기 (1)

# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

### max함수가 정렬보다 시간복잡도가 적을거라 생각해 작성한 코드
def solution(numbers):
    a = max(numbers)
    numbers.remove(a)
    b = max(numbers)
    return a*b

### 정렬로 풀이한 코드
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
