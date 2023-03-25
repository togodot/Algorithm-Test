### Lev.0 등수 매기기

# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다.
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

### 평균인데 총합으로 구했고, 너무 오래 고민했다. 딕셔너리 value를 기준으로 값을 비교하는데 오래 걸렸는데, 딕셔너리에 대한 이해가 부족함을 여실히 느꼈다.
def solution(score):
    sum_score = sorted([sum(i) for i in score], reverse=True)
    dic = {}

    for i in range(len(sum_score)):
        if sum_score[i] not in dic.values():
            dic[i+1] = sum_score[i]
    
    dic = dict(zip(dic.values(),dic.keys()))

    return [dic[sum(nums)] for nums in score]

### 반면, index 함수가 가장 앞의 값을 return하는 성질을 활용한 아주 간결한 코드도 있었다. 파이썬에 대해 제대로 이해한다면 훨씬 효율적인 코드 작성이 가능하다.
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
