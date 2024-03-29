### Lev.0 진료 순서 정하기

# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다.
# 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

### 응급도가 높은 순서대로 배열을 정렬한 후, 해당 값이 가지는 인덱스를 새 배열에 담아 반환한다. 1
def solution(emergency):
    a = sorted(emergency, reverse=True)
    return [a.index(i)+1 for i in emergency]
