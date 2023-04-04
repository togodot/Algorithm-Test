### Lev.0 7의 개수

# 머쓱이는 행운의 숫자 7을 가장 좋아합니다.
# 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

### array를 하나의 문자열로 바꾼 후 count함수로 7의 개수를 확인했다. 1
def solution(array):
    return ''.join(map(str, array)).count('7')

### 리스트 자체에 str함수가 적용된다는 사실을 새롭게 알게 되었다. 뿐만 아니라 하나의 문자열일 필요없이 리스트 내 전체 원소에 대해서 count함수가 적용된다.
def solution(array):
    return str(array).count('7')
