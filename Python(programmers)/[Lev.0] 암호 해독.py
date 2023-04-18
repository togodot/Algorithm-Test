### Lev.0 암호 해독

# 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.
# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

### range를 먼저 떠올렸다.
def solution(cipher, code):
    return ''.join(cipher[s] for s in range(code-1, len(cipher), code))

### 문자열 슬라이싱을 잘 활용하자. join 연산이 줄었다. 당연히도 시간 소요도 적음!
def solution(cipher, code):
    return cipher[code-1::code]
