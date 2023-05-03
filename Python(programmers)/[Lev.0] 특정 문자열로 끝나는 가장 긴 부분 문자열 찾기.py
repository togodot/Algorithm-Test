### Lev.0 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

# 문자열 myString과 pat가 주어집니다.
# myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

### 주어진 문자열의 뒤에서부터 탐색이 필요하다고 생각해 rfind를 사용했다. 2점
### rfind와 rindex의 차이: rfind는 찾는 값이 없을 경우 -1을 반환, rindex는 Exception(에러처리) 반환함
def solution(myString, pat):
    return myString[:myString.rfind(pat)] + pat
