### Lev.0 최빈값 구하기.py

# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.
# 최빈값이 여러 개면 -1을 return 합니다.

def solution(array):
    answer = -1
    check = {}
    for i in array:
        if i not in check:
            check[i] = 0
        check[i] += 1
    check = sorted(check.items(), key=lambda x:x[1], reverse=True)
    if (len(check) > 1 and check[0][1] != check[1][1]) or len(check) == 1:
        answer = check[0][0]
    return answer
  
  
  ### 내장함수를 적절하게 활용하는 방법도 필요 >> 더 간결한 코드 작성 가능
  def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
