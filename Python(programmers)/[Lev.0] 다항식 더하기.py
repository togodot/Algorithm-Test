### Lev.0 다항식 더하기

# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
# 다항식을 계산할 때는 동류항끼리 계산해 정리합니다.
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요.
# 같은 식이라면 가장 짧은 수식을 return 합니다.

### 실제 다항실 풀이하는 과정 그대로 코드를 작성했다. x 값들을 먼저 더한 후, 상수항 더하기. 무려 14점!을 받았다. isdigit과 같은 함수를 안 쓰는게 성능에 더 좋은걸까?싶다.
def solution(polynomial):
    p,n = 0,0
    for x in polynomial.split(' + '):
        if 'x' in x:
            if len(x) == 1:
                p += 1
            else:
                p += int(x[:-1])
        else:
            n += int(x)
    
    if p == 0 and n != 0:
        return f'{n}'
    elif p == 1:
        if n == 0:
            return 'x'
        else:
            return f'x + {n}'
    elif p > 1 and n == 0:
        return f'{p}x'
    else:
        return f'{p}x + {n}'
