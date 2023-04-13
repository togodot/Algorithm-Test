### Lev.1 달리기 경주

### 딕셔너리 두개로 푸는 것 같은데 이건 왜 안되는건지 아직 모르겠다.
def solution(players, callings):
    call_dict = {}
    for n in set(callings):
        call_dict[n] = callings.count(n)

    answer = players.copy()
    call_name = (i for i in players if i in call_dict.keys())

    for c in call_name:
        answer.remove(c)
        answer.insert(players.index(c)-call_dict[c], c)
    
    return answer
