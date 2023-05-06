### Lev.0 문자열이 몇 번 등장하는지 세기

# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

### in으로 확인하려다가 pat의 길이만큼 myString을 잘라서 직접 비교했다. 2점
def solution(myString, pat):
    cnt = 0
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            cnt += 1
    return cnt
