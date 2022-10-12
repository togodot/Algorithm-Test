### 14910번: 오르막

# 문제
# 주어진 N개의 정수가 비내림차순으로 나열되어 있는지 판정하는 프로그램을 작성하시오. N개의 수 A1, A2, ..., AN이 A1 ≤ A2 ≤ ... ≤ AN 을 만족하는 것을 비내림차순이라고 한다.
# 
# 입력
# 첫째 줄에 공백으로 구분된 N(1 ≤ N ≤ 1,000,000)개의 정수가 주어진다. 입력으로 주어지는 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 
# 출력
# 비내림차순으로 나열되어 있으면 Good을 출력하고, 그렇지 않으면 Bad을 출력한다.

N = list(map(int, input().split()))
ans = []
if len(N) == 1:
    ans.append(0)
else:
    for i in range(len(N)-1):
        if N[i] <= N[i+1]:
            ans.append(0)
        else:
            ans.append(1)
if sum(ans) == 0:
    print('Good')
else:
    print('Bad')
