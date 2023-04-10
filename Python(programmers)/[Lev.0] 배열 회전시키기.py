### Lev.0 배열 회전시키기

# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

### 조건문에 따라 슬라이싱과 '+'연산자로 리스트 이어붙이기
def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else:
        return numbers[1:] + [numbers[0]]

### 위 코드를 그대로 한 줄로 간단하게
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
