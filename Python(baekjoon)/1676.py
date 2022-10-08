### 1676번: 팩토리얼 0의 개수

# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
# 
# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.

N = int(input())
fanum = 1
for i in range(N):
    fanum *= (i+1)
ans = 0
for i in list(str(fanum)[::-1]):
    if i == '0':
        ans += 1
    else:
        break
print(ans)
