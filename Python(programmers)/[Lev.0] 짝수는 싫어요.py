### Lev.0 짝수는 싫어요
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    if n%2 == 0:
        for i in range(1, n//2+1):
            answer.append(2*i-1)
    else:
        for i in range(1, n//2+2):
            answer.append(2*i-1)
    return answer
