### Lev.0 무작위로 K개의 수 뽑기

# 랜덤으로 서로 다른 k개의 수를 저장한 배열을 만드려고 합니다.
# 적절한 방법이 떠오르지 않기 때문에 일정한 범위 내에서 무작위로 수를 뽑은 후, 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가하는 방식으로 만들기로 합니다.
# 이미 어떤 수가 무작위로 주어질지 알고 있다고 가정하고, 실제 만들어질 길이 k의 배열을 예상해봅시다.
# 정수 배열 arr가 주어집니다. 문제에서의 무작위의 수는 arr에 저장된 순서대로 주어질 예정이라고 했을 때, 완성될 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return 합니다.

### 중복이 없는 리스트 karr을 만들 때 첫 시도는 set함수를 사용하는 것이었는데, set 함수는 순서가 보장되지 않아 실패했다. 대신 딕셔너리의 키가 중복을 허용하지 않는다는 점을 이용했다. 2점
def solution(arr, k):
    karr = list(dict.fromkeys(arr))
    
    if len(karr) >= k:
        return karr[:k]
    else:
        return karr + [-1]*(k-len(karr))

### 리스트의 중복을 제거하되 기존 리스트의 순서를 유지하는 방법
### 1. Dictionary를 이용하는 방법: list(dict.fromkeys(dup_list))
### 2. Sorted() 함수를 이용하는 방법: sorted(set(dup_list), key=lambda x: dup_list.index(x))
### 3. Collection Package의 OrderedDict을 이용하는방법: from collections import OrderedDict >> list(OrderedDict.fromkeys(dup_list))
### 4. For문을 활용하는 방법:
###    num_list = []
###    for x in dup_list:
###        if x not in num_list:
###            num_list.append(x)
