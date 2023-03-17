### Lev.0 문자열 밀기
# 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다.
# 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때,
# A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.


### 원문자인 A를 한 칸씩 문자를 밀면서 B로 만들면서 B와 일치여부를 확인하는 코드를 작성했다.
def solution(A, B):
    cnt = 0
    
    while cnt != len(A):
        if A == B:
            return cnt
        A = A[-1]+A[:-1]
        cnt += 1
        
    return -1

### 문자를 민 B를 두 번 반복하면 그 배열 속에 결국은 A가 존재한다는 점과 find 함수에서 찾는 문자가 없는 경우 -1을 출력한다는 점을 활용한 멋진 코드를 발견했다.
def solution(A, B): return (B * 2).find(A)

### 위 코드를 lambda 함수를 활용해 더 간단하게 한 코드.
solution=lambda a,b:(b*2).find(a)
