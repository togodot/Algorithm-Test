### Lev.1 약수의 개수와 덧셈

# 두 정수 left와 right가 매개변수로 주어집니다.
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

### 문제 그대로 범위 내 각 숫자들의 약수의 갯수를 구한 후, 짝/홀에 따라 값을 더하고 빼줬다.
def solution(left, right):
    ans = 0
    for num in range(left, right+1):
        div = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                div += 1
                if i != (num//i):
                    div += 1
        if div % 2 == 0:
            ans += num
        else:
            ans -= num
    
    return ans

### 문제를 제대로 이해해보면, 약수의 개수가 홀수인 값은 제곱수라는 점을 생각해내면 약수의 개수를 직접 구하고 홀/짝을 구분하는 코드가 생략된다. >> 단순히 문제 그대로 구현하기보다, 문제의 '내용'을 제대로 이해하는 것이 중요함을 다시 한 번 느끼게 한다.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
