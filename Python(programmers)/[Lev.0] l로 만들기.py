### Lev.0 l로 만들기

# 알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.

### 문자를 숫자로 변환하지 않고, 문자열 자체의 대소 비교가 가능하다는 점을 활용했다. 1점
def solution(myString):
    return ''.join(x if x > 'l' else 'l' for x in myString)

### translate 함수를 사용하는 방법 또한 있다.  >>>  str.maketrans('바꿀문자', '새문자')
def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))
