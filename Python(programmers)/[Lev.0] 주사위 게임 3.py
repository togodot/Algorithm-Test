### Lev.0 주사위 게임 3

# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
# 
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

### 각 숫자의 갯수가 담긴 리스트 cnt를 먼저 생성한 후 cnt의 값을 조건문으로 각각 비교했다. 2점
def solution(a, b, c, d):
    lst = [a, b, c, d]
    cnt = [lst.count(i) for i in lst]
    if max(cnt) == 4:
        return 1111 * a
    elif max(cnt) == 3:
        return (10*lst[cnt.index(3)] + lst[cnt.index(1)]) ** 2
    elif max(cnt) == 2:
        if min(cnt) == 2:
            x, y = max(lst), min(lst)
            return (x+y) * abs(x-y)
        else:
            temp = [i for i in lst if i != lst[cnt.index(2)]]
            return temp[0] * temp[1]
    else:
        return min(lst)
