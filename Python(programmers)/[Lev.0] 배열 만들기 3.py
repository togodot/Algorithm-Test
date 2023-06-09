### Lev.0 배열 만들기 3

# 정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.
# intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.
# 이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.

### 리스트를 합치는 세 가지 방법(+, extend, sum) 중 sum을 사용했다. sum 함수의 기본형이 sum(덧셈할 것, 처음에 더할 것)인 점을 활용해 두 리스트를 합했다. 1점
def solution(arr, intervals):
    return sum((arr[i:j+1] for i,j in intervals),[])
