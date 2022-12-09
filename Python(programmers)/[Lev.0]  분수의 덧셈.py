### Lev.0 분수의 덧셈
# 첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다.
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(denum1, num1, denum2, num2):
    denum3 = num1*denum2 + num2*denum1
    num3 = num1 * num2
    
    for i in range(1, denum3+1):
        if num3%i==0 and denum3%i==0:
            gcd = i
    answer = [int(denum3/gcd), int(num3/gcd)]
    return answer
