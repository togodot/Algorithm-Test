### Lev.0 잘라서 배열로 저장하기

# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

### n의 간격을 고려함과 동시에 마지막 남은 문자열을 그대로 출력하는 코드를 작성
def solution(my_str, n):
    answer = []
    nums = len(my_str)//n if len(my_str)%n == 0 else len(my_str)//n +1
    for i in range(nums):
        if i != nums:
            answer.append(my_str[n*i:n*(i+1)])
        else:
            answer.append(my_str[n*i:])
    return answer

### 슬라이싱은 초과해도 에러가 나지 않는다는 점을 활용. n의 간격을 range에서 잘 사용한 코드다.
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
