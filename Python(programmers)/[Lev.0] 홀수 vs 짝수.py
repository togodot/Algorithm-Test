### Lev.0 홀수 vs 짝수

# 정수 리스트 num_list가 주어집니다.
# 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요.
# 두 값이 같을 경우 그 값을 return합니다.

### 두 값의 대소를 구분할 때, 단순 대소 구분이라면 max 함수를 쓸 수 있다. 1점
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
