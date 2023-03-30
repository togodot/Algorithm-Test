### Lev.1 가운데 글자 가져오기

# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

### 단순하게 홀수인지 짝수인지 if문으로 비교하여 결과 반환
def solution(s):
    answer = s[len(s)//2] if len(s)%2 != 0 else s[len(s)//2 -1:len(s)//2+1]
    return answer

### 파이썬의 index 함수가 정수만 반환한다는 점을 활용하면 홀/짝 구분이 필요 없어진다!
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]
