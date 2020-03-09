import sys
sys.stdin = open('input.txt')

def search(month, price):
    global min_price
    if month > 11:
        if min_price > price:
            min_price = price
    elif price >= min_price:
        return
    else:
        if monthly_usage[month]:
            search(month+1, price + min(plan[0] * monthly_usage[month], plan[1]))
            search(month+3, price + plan[2])
        else:
            search(month+1, price)

t = int(input())
for test_case in range(1, t+1):
    plan = list(map(int, input().split()))    # daily, one_month, three_month, annual
    monthly_usage = list(map(int, input().split()))
    min_price = plan[3]
    search(0, 0)
    print('#{} {}'.format(test_case, min_price))