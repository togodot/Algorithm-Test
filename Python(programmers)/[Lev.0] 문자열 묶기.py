### Lev.0 문자열 묶기

# 문자열 배열 strArr이 주어집니다.
# strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

### 원소의 길이와 갯수를 딕셔너리에 저장한 후 최댓값을 찾는 방법이다. 3점!
def solution(strArr):
    len_dict = {}

    for s in strArr:
        if len(s) not in len_dict:
            len_dict[len(s)] = 1
        else:
            len_dict[len(s)] += 1

    return max(len_dict.values())

### strArr의 최대 원소 길이가 30이라는 제한사항을 이용한 풀이방법이다. 하나의 원소의 길이를 인덱스 값으로 설정했다.
def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)
