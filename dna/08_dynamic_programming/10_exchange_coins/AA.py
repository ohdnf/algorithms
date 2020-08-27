import sys
# sys.stdin = open('in3.txt')

n = int(input())    # 동전의 종류 수
coin = list(map(int, input().split()))  # 동전의 종류
m = int(input())    # 거슬러 줄 금액

dp = [0] + [501] * m    # x원을 거슬러 주는 데 사용된 동전의 최소 개수(0원은 0개로 초기화)

for i in range(n):
    for j in range(coin[i], m+1):
        dp[j] = min(dp[j], dp[j-coin[i]]+1)

print(dp[m])