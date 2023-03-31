### Lev.0 중복된 문자 제거

# 문자열 my_string이 매개변수로 주어집니다.
# my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

### 중복이 없는 문자를 리스트에 담고 포함여부를 확인하는 코드 작성. 1점..
def solution(my_string):
    answer = []
    for s in my_string:
        if s not in answer:
            answer.append(s)
    return ''.join(answer)

### 리스트가 필요 없었다.
def solution(my_string):
    answer = ''
    for s in my_string:
        if s not in answer:
            answer += s
    return answer

### 딕셔너리 생성 메서드인 dict.fromkeys를 사용하여 훨씬 효율적이고 직관적인 코드 작성이 가능하다.
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
