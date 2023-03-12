def solution(sides):
    answer = (1 if max(sides) < (sum(sides) - max(sides)) else 2)
    return answer
