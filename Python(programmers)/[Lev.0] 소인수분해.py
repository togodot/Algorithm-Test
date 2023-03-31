### Lev.0 소인수분해

# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다.
# 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다.
# 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

### 2부터 반복하여 나눈 값으로 소인수를 구한 후 set으로 중복을 제거했다. set를 배열로 변환한 값을 반환했더니 틀린 닶이 생겼고, 배열을 다시 정렬하니 해결됐다. 4점!
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            answer.append(d)
        else:
            d += 1
    return sorted(list(set(answer)))
