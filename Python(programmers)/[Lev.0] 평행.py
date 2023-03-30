### Lev.0 평행

# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

### (y2-y1)/(x2-x1)라는 수식을 여러 차례 반복하는 것을 간결하게 하는 방법을 찾다가, 단 네 개의 점만을 비교하면 되는 문제이므로 단순 나열하여 해결했다. +8점!!
def solution(dots):    
    if (dots[0][1]-dots[1][1])/(dots[0][0]-dots[1][0]) == (dots[2][1]-dots[3][1])/(dots[2][0]-dots[3][0]):
        return 1
    if (dots[0][1]-dots[2][1])/(dots[0][0]-dots[2][0]) == (dots[1][1]-dots[3][1])/(dots[1][0]-dots[3][0]):
        return 1
    if (dots[0][1]-dots[3][1])/(dots[0][0]-dots[3][0]) == (dots[1][1]-dots[2][1])/(dots[1][0]-dots[2][0]):
        return 1
    return 0
