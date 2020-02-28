import sys
sys.stdin = open('input.txt')

def scan(month, price):
    global min_price
    global three
    if month >= 12:
        if price < min_price:
            min_price = price
    elif price > min_price:
        return
    else:
        scan(month+3, price - price_three[month] + three)
        scan(month+1, price)

t = int(input())
for test_case in range(1, t+1):
    day, one, three, year = map(int, input().split())
    annual_plan = list(map(int, input().split()))
    prices = [0] * 14
    # (한달 사용량 * 1일권) vs. 1개월권
    for month in range(12):
        if annual_plan[month] > 0:
            if day * annual_plan[month] < one:
                prices[month] = day * annual_plan[month]
            else:
                prices[month] = one
    min_price = sum(prices)
    # (세 달 사용량 * 각 월 이용권) vs. 3개월권
    price_three = [sum(prices[start:start+3]) for start in range(12)]
    scan(0, min_price)
    # 1년권
    if year < min_price:
        min_price = year
    print('#{} {}'.format(test_case, min_price))