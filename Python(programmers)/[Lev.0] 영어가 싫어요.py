### Lev.0 영어가 싫어요
# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for n in range(len(nums)):
        numbers = numbers.replace(nums[n], str(n))
    answer = int(numbers)
    return answer
  

### enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)을 만들어준다.
def solution(numbers):
    for num, enum in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(enum, str(num))
    return int(numbers)
