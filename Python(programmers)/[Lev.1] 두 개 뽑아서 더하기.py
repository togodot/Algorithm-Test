### Lev.1 두 개 뽑아서 더하기
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    import itertools
    set_list = itertools.permutations(numbers, 2)
    set_list = list(set_list)
    sum_set = set()
    for setnum in set_list:
        sum_set.add(sum(setnum))
    sum_list = list(sum_set)
    sum_list.sort()
    answer = sum_list
    return answer
