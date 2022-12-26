### Lev.1 시저 암호

# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

def solution(s, n):
    res = ''
    for i in range(len(s)):
        m = ord(s[i])
        if m == 32:
            res += ' '
        elif m >= 65 and m <= 90:
            if m+n > 90:
                res += chr(m+n-26)
            else:
                res += chr(m+n)
        else:
            if m+n > 122:
                res += chr(m+n-26)
            else:
                res += chr(m+n)
    answer = res
    return answer
