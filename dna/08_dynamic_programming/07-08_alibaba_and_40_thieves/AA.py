from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')
# sys.stdin = open('dna/08_dynamic_programming/07-08_alibaba_and_40_thieves/in1.txt')

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

# Bottom-up
dp = [[0]*n for _ in range(n)]

# 0행, 0열의 값들 초기화
dp[0][0] = cost[0][0]
for i in range(1, n):
    dp[0][i] = dp[0][i-1] + cost[0][i]
    dp[i][0] = dp[i-1][0] + cost[i][0]

# 최단거리로 이동한다.
for row in range(1, n):
    for col in range(1, n):
        dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + cost[row][col]

print(dp[n-1][n-1])

# Top-down
