### Lev.0 원소들의 곱과 합
# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

### 모든 원소를 곱하는 과정을 가급적 일찍 멈추기 위해 if문을 for문 중간에 사용했는데, 혹시 성능을 더 떨어트린건 아닐까. 1점
def solution(num_list):
    x = num_list[0]
    for n in num_list[1:]:
        x *= n
        if x > sum(num_list)**2:
            return 0
    return 1
