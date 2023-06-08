### Lev.0 원하는 문자열 찾기

# 알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.
# 단, 알파벳 대문자와 소문자는 구분하지 않습니다.

### if else 조건문을 통해 결과값을 반환했다. 1점
def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0

### in/not in의 결과값이 bool값이라는 점을 활용할 수 있다. if 조건문:반환결과값을 설정할 필요 없이 bool 값에 따라 문제에서 요구하는 결과값인 1, 0을 반환할 수 있다.
def solution(myString, pat):
    return int(pat.lower() in myString.lower())
