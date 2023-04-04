### Lev.0 이진수 더하기

# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

### 이진수->십진수 변환후 더하여 다시 이진수 변환. format('b'가 이진수, 'd'가 십진수) 함수 활용
def solution(bin1, bin2): return format((int(bin1,2) + int(bin2,2)), 'b')

### 같은 방법. 이진수로 바꾸는 bin() 함수 사용. 단, bin 사용시 앞에 0b가 붙으므로 [2:]로 슬라이싱
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer
