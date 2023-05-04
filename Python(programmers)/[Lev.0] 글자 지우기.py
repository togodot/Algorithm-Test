### Lev.0 글자 지우기

# 문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

### 인덱스가 유지되어야하기 때문에 인덱스와 값을 딕셔너리로 만든 후, 처리했다. 1
def solution(my_string, indices):
    str_dict = dict(enumerate(my_string))

    for idx in indices:
        del str_dict[idx]

    return ''.join(str_dict.values())

### dict를 따로 만들지 않고 바로 enumerate한 인덱스와 값을 사용할 수 있었다. 제한범위가 크지 않아서 성능 차이는 크지 않았다.
def solution(my_string, indices):
    return ''.join(a for i, a in enumerate(my_string) if i not in indices)
