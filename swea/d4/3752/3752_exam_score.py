import sys
sys.stdin = open('input.txt')

def dfs(i, k, score):
    if i == k:
        scores.add(score)
    else:
        dfs(i+1, k, score+allots[i])
        dfs(i+1, k, score)

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    allots = list(map(int, input().split()))
    scores = set()

    # dfs(0, n, 0)

    # for i in range(1<<n):
    #     score = 0
    #     for j in range(n):
    #         if i & (1<<j):
    #             score += allots[j]
    #     scores.add(score)

    

    print('#{} {}'.format(test_case, len(scores)))
