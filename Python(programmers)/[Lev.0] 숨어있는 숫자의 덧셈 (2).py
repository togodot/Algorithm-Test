### Lev.0 숨어있는 숫자의 덧셈 (2)

# 문자열 my_string이 매개변수로 주어집니다.
# my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

### isdigit 함수로 숫자만 남긴 후 공백으로 대체된 문자열 부분을 삭제한 리스트를 합한다. 4점!
def solution(my_string):
    nums = ''.join([i if i.isdigit() else ' ' for i in my_string]).split()
    return sum(list(map(int, nums)))

### list에 담을 필요 없이 해결하는 방법
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())
