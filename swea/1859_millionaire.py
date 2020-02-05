# T = int(input())
# for test_case in range(1, T + 1):
#     days = int(input())
#     prices = list(map(int, input().split()))
#     profit = 0
#     while len(prices) > 1:
#         max_price = max(prices)
#         max_index = prices.index(max_price)
#         profit += max_price * len(prices[:max_index]) - sum(prices[:max_index])
#         del prices[:max_index + 1]
#         # sell = prices.pop(0)
#         # if max_price > sell:
#         #    profit += max_price - sell
#     print('#{0} {1}'.format(test_case, profit))


# Other Solution
n = int(input())
 
for ni in range(n):
    cnt = int(input())
    a = list(map(int, input().split()))
    res = 0
    i = cnt-1
   
    while i > 0:
        j = i-1
        c=0
        while a[j]<a[i] and j >=0:
            c += 1
            res -= a[j]
            j -= 1
        res += (c*a[i])
        i -= (c+1)
    print(f'#{ni+1} {res}')