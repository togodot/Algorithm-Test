### Lev.1 숫자 짝꿍

# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다
# (단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다).
# X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.
# 예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다.
# 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다
# (X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

### 각 숫자의 등장 횟수를 count하여 딕셔너리에 넣은 후, set함수로 키의 교집합의 값의 최솟값들을 가져왔다. 7점!
def solution(X, Y):
    x_dic = {}
    y_dic = {}
    res = ''

    for i in set(X):
        x_dic[i] = X.count(i)
    for j in set(Y):
        y_dic[j] = Y.count(j)
    for k in set(X) & set(Y):
        res += k * min(x_dic[k],y_dic[k])
    ans = ''.join(sorted(res, reverse=True))
    
    if set(ans) == {'0'}:
        return '0'
    elif len(ans) > 0:
        return ans
    else:
        return '-1'

### 위의 방식을 Counter 함수를 사용하는 방법
from collections import Counter
def solution(X, Y):
    x_dic = Counter(list(X))
    y_dic = Counter(list(Y))
    res = ''

    for k in set(X) & set(Y):
        res += k * min(x_dic[k],y_dic[k])

    ans = ''.join(sorted(res, reverse=True))

    if set(ans) == {'0'}:
        return '0'
    elif len(ans) > 0:
        return ans
    else:
        return '-1'

### range(9,-1,-1)를 사용한다면 정렬 과정이 생략되어 좋다
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
