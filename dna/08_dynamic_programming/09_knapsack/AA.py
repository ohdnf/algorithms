import sys
# sys.stdin = open('in4.txt')

NUMBER_OF_JEWEL, MAX_WEIGHT = map(int, input().split())    # 보석 개수(<=30), 가방 저장 무게(<1000)
dp = [0] * (MAX_WEIGHT+1)
for _ in range(NUMBER_OF_JEWEL):
    weight, value = map(int, input().split()) # 보석의 무게, 가치
    for k in range(weight, MAX_WEIGHT+1):
        dp[k] = max(dp[k-weight]+value, dp[k])

print(dp[MAX_WEIGHT])