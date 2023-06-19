### Lev.0 정수 찾기

# 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

### 한줄 if문에서 in을 사용해 확인했다. 1점
def solution(num_list, n):
    return 1 if n in num_list else 0

### bool 값을 int로 변환하는 방법도 있다.
def solution(num_list, n):
    return int(n in num_list)
