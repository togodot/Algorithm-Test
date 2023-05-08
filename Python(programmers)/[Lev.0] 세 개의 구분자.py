### Lev.0 세 개의 구분자

# 

###
def solution(myStr):
    str_lst = myStr.replace('b','a').replace('c','a').split('a')
    if len([i for i in str_lst if len(i) > 0]) > 0:
        return [i for i in str_lst if len(i) > 0]
    else:
        return ["EMPTY"]

### 
def solution(myStr):
    answer = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    return answer if answer else ['EMPTY']
