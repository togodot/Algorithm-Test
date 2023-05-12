### Lev.0 빈 배열에 추가, 삭제하기

# 아무 원소도 들어있지 않은 빈 배열 X가 있습니다.
# 길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고,
# flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.

### 리스트에 원소를 추가할 땐 + 연산, 원소를 제거할 땐 리스트 슬라이싱을 활용했다. 1점
def solution(arr, flag):
    answer = []
    for i, b in enumerate(flag):
        if b == True:
            answer += [arr[i]] * arr[i] * 2
        else:
            answer = answer[:-arr[i]]
    return answer

### 위와 같은 풀이에 zip함수를 사용한 방법
def solution(arr, flag):
    arr1 = []
    for i, j in zip(arr, flag):
        if j:
            arr1 += [i] * i * 2
        else:
            arr1 = arr1[:-i]
    return arr1
