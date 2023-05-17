### Lev.0 순서 바꾸기

# 정수 리스트 num_list와 정수 n이 주어질 때, num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.

### 리스트 슬라이싱과 + 연산 활용. 1점
def solution(num_list, n):
    return num_list[n:] + num_list[:n]
