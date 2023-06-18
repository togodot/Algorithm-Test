### Lev.0 수 조작하기 1

# 정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.
# 
# "w" : n이 1 커집니다.
# "s" : n이 1 작아집니다.
# "d" : n이 10 커집니다.
# "a" : n이 10 작아집니다.
# 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

### dict 형태로 매치시킨 후 count로 연산을 줄이고자 했다. 1점
def solution(n, control):
    dic = {'w':1, 's':-1, 'd':10, 'a':-10}
    return n + sum(control.count(s)*dic[s] for s in 'wsda')

### dict로 직접 매칭하지 않고 키와 값을 리스트 형태로 전달하는 dict 함수 사용
def solution(n, control):
    dic = dict(zip('wsda', [1,-1,10,-10]))
    return n + sum(control.count(s)*dic[s] for s in 'wsda')
