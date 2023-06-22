### Lev.0 공배수

# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

### number에서 두 정수 n,m을 나눈 값을 비교하는 조건문 사용. 1점
def solution(number, n, m):
    return 1 if number%n==0 and number%m==0 else 0

### if문 대신 bool을 사용하는 방법(조건이 참일 때 1, 거짓일 때 0을 리턴하므로)
def solution(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))
