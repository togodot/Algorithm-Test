### Lev.0 배열 만들기 2

# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

### 0,5로만 구성되었는지 판단하기 위해 all함수를 사용하고자 했다. 0,5외의 값을 False로 만들어 확인하는 방식을 사용했다. 1점
def solution(l, r):
    import re
    answer = []
    
    for i in range(l, r+1):
        num = str(i).replace('0','5')
        num = re.sub('(1|2|3|4|6|7|8|9)','0',num)
        if all(list(map(int, list(num)))) == True:
            answer.append(i)

    if len(answer) > 0:
        return answer
    else:
        return [-1]

### 0,5로 구성되었는지 확인하기 위해 set를 활용하는 방법이다. set를 통해 중복을 없앤 후 set의 특징인 차집합을 활용해 0,5가 아닌 숫자를 걸러냈다. 앞선 풀이보다 성능이 조금 더 빠르다.
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]
