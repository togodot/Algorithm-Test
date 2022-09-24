### 25591번: 푸앙이와 종윤이

# 문제
# 푸앙이의 친구 종윤이는 수학, 과학이 굉장히 발전한 곳 중 하나인 인도에 진심이다. 한국에선 구구단을 배우지만 인도에서는 19단까지 배운다고 한다. 어떻게 두 자릿수 곱셈을 빠르게 암산하는 것일까? 푸앙이는 인도 마니아 종윤이한테 인도의 베다수학 곱셈법을 배워보기로 했다.

# 97×96을 계산해보자. 각 수를 100에서 빼준 값을 a, b라고 하면 
# a = 100-97 = 3
# b = 100-96 = 4
# 그리고 c, d를 다음과 같이 정의하고 구한다.
# c = 100-(a+b) = 100-7 = 93
# d = a×b = 3×4 = 12
# c는 곱셈 결괏값의 앞의 두 자릿수, d는 뒤의 두 자릿수에 해당한다.

# a, b가 작을 때는 위와 같은 계산으로 끝나지만 그렇지 않은 경우도 존재한다. 만약 d가 두 자릿수를 넘어버린다면 다시 여기서 하위 두 자릿수만 취하고, 초과 자릿수들의 값은 c에 더해주면 된다.
# 다시 말해서, d를 100으로 나눈 몫과 나머지를 각각 q, r이라고 했을 때 c+q를 앞의 두 자릿수, r을 뒤의 두 자릿수로 결정한다.
# 푸앙이도 인도에 흥미가 생겼지만, 수학은 머리가 아프다. 푸앙이를 위해서 두 수가 들어왔을 때 인도의 베다수학 곱셈법을 자동으로 계산해주는 프로그램을 만들어주자.

# 입력
# 한 줄에 양의 정수가 2개 주어진다. 이 정수들은 10 이상 100 미만의 두 자릿수다.

# 출력
# 베다수학 곱셈법을 쓰는 과정에서 구하는 a, b, c, d, q, r을 첫 줄에 공백으로 구분해서 출력한다. 둘째 줄에 곱셈 결과의 앞의 두 자릿수, 뒤의 두 자릿수를 공백으로 구분해서 출력한다. 만약 이 수들의 십의 자리가 0이라면 일의 자리만 출력한다.

x, y = map(int, input().split())
a = 100 - x
b = 100 - y
c = 100 - (a + b)
d = a * b
q = d//100
r = d%100
print(a, b, c, d, q, r)
print(c+q, r)
