import sys
sys.stdin = open('in3.txt')

n, m = map(int, input().split())    # 문항 개수, 제한 시간

# 문항은 안 풀었을 때를 0으로 초기화
point = [0]  # 문항 배점
ets = [0]    # 문항 당 풀이 시간
for _ in range(n):
    p, e = map(int, input().split())
    point.append(p)
    ets.append(e)

# dp = [[0] * (m+1) for _ in range(n+1)]   # 0~m시간이 주어지고 n번 문항까지 선택했을 때 최대 점수

# for i in range(1, n+1):
#     for t in range(ets[i], m+1):
#         dp[i][t] = max(dp[i-1][t-ets[i]]+point[i], dp[i-1][t])

# print(max(dp[-1]))
# print(dp[-1][-1])


dp = [0] * (m+1)

for i in range(1, n+1):
    for t in range(m, ets[i]-1, -1):    # 거꾸로 탐색하면 중복이 되지 않음
        dp[t] = max(dp[t-ets[i]]+point[i], dp[t])

print(dp[m])