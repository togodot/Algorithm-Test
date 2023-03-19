def solution(dots):
    w = max([dots[i][0] for i in range(4)]) - min([dots[i][0] for i in range(4)])
    l = max([dots[i][1] for i in range(4)]) - min([dots[i][1] for i in range(4)])
    return w*l
