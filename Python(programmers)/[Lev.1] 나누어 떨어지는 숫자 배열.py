### Lev.1 나누어 떨어지는 숫자 배열

# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

def solution(arr, divisor):
    res = []
    for i in arr:
        if i % divisor == 0:
            res.append(i)
    if len(res) >= 1:
        res.sort()
    else:
        res = [-1]
    answer = res
    return answer
