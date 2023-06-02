### Lev.0 배열 만들기 6

# 0과 1로만 이루어진 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk을 만드려고 합니다.
# i의 초기값을 0으로 설정하고 i가 arr의 길이보다 작으면 다음을 반복합니다.
# 만약 stk이 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
# stk에 원소가 있고, stk의 마지막 원소가 arr[i]와 같으면 stk의 마지막 원소를 stk에서 제거하고 i에 1을 더합니다.
# stk에 원소가 있는데 stk의 마지막 원소가 arr[i]와 다르면 stk의 맨 마지막에 arr[i]를 추가하고 i에 1을 더합니다.
# 위 작업을 마친 후 만들어진 stk을 return 하는 solution 함수를 완성해 주세요.
# 단, 만약 빈 배열을 return 해야한다면 [-1]을 return 합니다.

### 마지막 원소를 제거하는 과정을 슬라이싱, del, pop 모두 비교해보았는데 del이 조금 더 나은 성능을 보여서 택했다. arr이 0과 1로만 이루어졌다는 점에서 다른 풀이법도 더 생각해봐야겠다. 1점
def solution(arr):
    stk = []

    for i in range(len(arr)):
        if len(stk) == 0 or stk[-1] != arr[i]:
            stk.append(arr[i])
        else:
            del stk[-1]
            
    return stk if stk else [-1]

### 위의 풀이와 비슷한 흐름이지만 and와 or과 같은 논리연산을 적극 활용한 방법이다.
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]
