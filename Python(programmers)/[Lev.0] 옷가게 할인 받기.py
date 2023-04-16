### Lev.0 옷가게 할인 받기

# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
# 
# 제한사항
# 10 ≤ price ≤ 1,000,000
# price는 10원 단위로(1의 자리가 0) 주어집니다.
# 소수점 이하를 버린 정수를 return합니다.

### 할인율이 적용되는 각각의 가격 범위에 대해 할인율을 곱해주었다. 2점
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    return price

### 가격대별 할인율을 미리 딕셔너리에 저장한 후, 가격과 딕셔너리 키를 비교하여 가격에 딕셔너리 값을 곱해주는 방식이다.
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
