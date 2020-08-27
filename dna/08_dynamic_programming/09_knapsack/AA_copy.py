import sys
sys.stdin = open('in0.txt')

NUMBER_OF_JEWEL, MAX_WEIGHT = map(int, input().split())    # 보석 개수(<=30), 가방 저장 무게(<1000)
weight = [0]
value = [0]
for _ in range(NUMBER_OF_JEWEL):
    w, v = map(int, input().split()) # 보석의 무게, 가치
    weight.append(w)
    value.append(v)

dp = [[-1]*(MAX_WEIGHT+1) for _ in range(NUMBER_OF_JEWEL+1)]

def knapsack():
    for i in range(NUMBER_OF_JEWEL+1):
        dp[i][0] = 0
    for w in range(MAX_WEIGHT+1):
        dp[0][w] = 0
    
    for i in range(1, NUMBER_OF_JEWEL+1):
        for w in range(1, MAX_WEIGHT+1):
            if weight[i] > w:   # i번 물건을 담을 수 없는 경우
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w-weight[i]]+value[i], dp[i-1][w])
    return dp[NUMBER_OF_JEWEL][MAX_WEIGHT]

print(knapsack())

for line in dp:
    print(line)

# jewel = [list(map(int, input().split())) for _ in range(NUMBER_OF_JEWEL)]
# jewel.append([0, 0])
# jewel.sort(key=lambda j: j[0])

# dp = [[-1]*(MAX_WEIGHT+1) for _ in range(NUMBER_OF_JEWEL+1)]

# def knapsack(i, W):
#     if dp[i][W] != -1:
#         return dp[i][W]
    
#     if i == 0 or W == 0:
#         dp[i][W] = 0
#         return dp[i][W]
#     else:
#         case1 = 0
#         if W >= jewel[i][0]:
#             case1 = knapsack(i-1, W-jewel[i][0]) + jewel[i][1]
        
#         case2 = knapsack(i-1, W)

#         dp[i][W] = max(case1, case2)
#         return dp[i][W]


# res = knapsack(NUMBER_OF_JEWEL, MAX_WEIGHT)
# print(res)
