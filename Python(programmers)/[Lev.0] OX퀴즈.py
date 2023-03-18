### Lev.0 OX퀴즈
# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

### 세 번째 코드에서부터 차례로 코드 길이를 줄여나갔다.
def solution(quiz):
    answer = ['O' if eval(q.split('=')[0]) == int(q.split('=')[1]) else 'X' for q in quiz]
    return answer

### '='로 split한 값을 각 각의 변수에 저장
def solution(quiz):
    answer = []
    for q in quiz:
        x, y = q.split('=')
        answer.append('O' if eval(x) == int(y) else 'X')

    return answer

### 문제를 처음보고 든 생각의 순서 그대로 코드 
def solution(quiz):
    answer = []
    for q in quiz:
        if eval(q.split('=')[0]) == int(q.split('=')[1]):
            answer.append('O')
        else:
            answer.append('X')
    
    return answer
