### Lev.0 저주의 숫자 3

# 
def solution(n):
    lst = []
    num = 0
    while len(lst) != n:
        num += 1
        if num%3 != 0 and '3' not in str(num):
            lst.append(num)
    return lst[-1]
