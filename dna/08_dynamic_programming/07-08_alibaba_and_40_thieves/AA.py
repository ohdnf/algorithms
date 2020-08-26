from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in2.txt')
# sys.stdin = open('dna/08_dynamic_programming/07-08_alibaba_and_40_thieves/in1.txt')

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
# 0행, 0열의 값들 초기화
dp[0][0] = cost[0][0]
for i in range(1, n):
    dp[0][i] = dp[0][i-1] + cost[0][i]
    dp[i][0] = dp[i-1][0] + cost[i][0]


# Bottom-up
# for row in range(1, n):
#     for col in range(1, n):
#         # 최단거리로 이동하므로 오른쪽 또는 아래 방향으로만 움직인다.
#         dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + cost[row][col]
# print(dp[n-1][n-1])

# Top-down

def dfs(row, col):
    # Memoization
    if dp[row][col]:
        return dp[row][col]

    if row == 0 and col == 0:
        dp[row][col] = cost[row][col]
    elif row == 0:
        dp[row][col] = dfs(row, col-1) + cost[row][col]
    elif col == 0:
        dp[row][col] = dfs(row-1, col) + cost[row][col]
    else:
        dp[row][col] = min(dfs(row-1, col), dfs(row, col-1)) + cost[row][col]
    return dp[row][col]


print(dfs(n-1, n-1))