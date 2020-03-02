## 항래쓰

T=int(input())
for tc in range(1,T+1):
    prices= list(map(int,input().split()))
    count_per_month=list(map(int,input().split()))
    calc_prices=[ prices[1] if prices[1]/prices[0]<x else prices[0]*x for x in count_per_month]
    min_sum=prices[3]
    def combi(level,s):
        global min_sum
        if level==12:
            if s<min_sum:
                min_sum=s
            return
        else:
            combi(level+1, s+calc_prices[level])
            last=min(11, level+2)
            three_month_price=sum(calc_prices[level:last+1])
            if three_month_price> prices[2]:
                combi(last+1,s+prices[2])
    combi(0,0)
    print('#{} {}'.format(tc,min_sum))



## 태우쓰

def dfs(month, cost):
    global min_cost
    if month > 12:
        # 최소 비용 계산
        if cost < min_cost:
            min_cost = cost
        return
    if cost > min_cost:
        return
    if plan[month]:
        dfs(month+1, cost + plan[month] * d)
        dfs(month+1, cost + m)
        dfs(month+3, cost + t)
    else:
        dfs(month+1, cost)
 
T = int(input())
for tc in range(1, T+1):
    d,m,t,y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    min_cost = y
    dfs(1, 0)
    print("#{} {}".format(tc, min_cost))



## 윤지쓰

T = int(input())
for tc in range(1, T+1):
    fare = list(map(int, input().split()))
    d = list(map(int, input().split()))
    # print(d)
    dp = [0]*12
    dp[0] = min(fare[0]*d[0], fare[1])
    for i in range(1, 12):
        dp[i] = min(dp[i-1]+d[i]*fare[0], dp[i-1]+fare[1])
        if i >= 2:
            dp[i] = min(dp[i-3]+fare[2], dp[i])
    result = min(dp[11], fare[3])
    print(f'#{tc} {result}')