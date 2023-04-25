### Lev.0 문자 개수 세기

# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때,
# my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수,
# my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.

### 대소문자일 경우를 분리하지 않고 한번에 구한 후, 대문자와 소문자 사이 7개의 아스키코드 부분을 리스트 슬라이싱과 연결로 해결했다.
def solution(my_string):
    answer = [0] * 58
    for c in my_string:
        answer[ord(c)-65] += 1
    return answer[:26] + answer[32:]
