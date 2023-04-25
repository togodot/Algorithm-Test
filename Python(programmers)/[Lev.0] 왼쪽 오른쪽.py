### Lev.0 왼쪽 오른쪽

# 문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다.
# str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를,
# 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# "l"이나 "r"이 없다면 빈 리스트를 return합니다.

### 문자열 리스트가 최대 20으로 제한사항이 있기 때문에 길지 않으므로 for문으로 처음부터 탐색하는 방법을 선택했다. 16점 ?!
def solution(str_list):
    for i, c in enumerate(str_list):
        if c == 'l':
            return str_list[:i]
        if c == 'r':
            return str_list[i+1:]
    return []
