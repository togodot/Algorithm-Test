### Lev.1 옹알이 (2)

# 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다.
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다.
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

### 발음이 연속되지 않고 반복될 경우 발음이 가능하다는 점! +10!!
def solution(babbling):
    answer = 0
    for b in babbling:
        for c in ["aya", "ye", "woo", "ma"]:
            if b.find(c*2) == -1:
                b = b.replace(c,' ')
        if len(b.split()) == 0:
            answer += 1
    return answer
