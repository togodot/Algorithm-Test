### Lev.0 문자열의 뒤의 n글자

# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

### 슬라이싱 시작점을 정하기 위해 my_string에서 n을 뺐다. 1점
def solution(my_string, n):
    return my_string[len(my_string)-n:]

### 슬라이싱에서 시작점을 음수로 설정하면 애초에 뒤에서부터 카운트한 위치에서 시작한다는 점. len 연산을 줄일 수 있었다.
def solution(my_string, n):
    return my_string[-n:]
