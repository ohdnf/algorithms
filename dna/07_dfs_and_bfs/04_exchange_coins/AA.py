import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

t = int(input())    # 지폐 금액
k = int(input())    # 동전 가짓수
coin = [list(map(int, input().split())) for _ in range(k)]  # 동전 금액, 동전 갯수

coin.sort(key=lambda c: (-c[0], c[1]))  # 금액이 큰 동전, 갯수가 적은 동전 순으로 정렬

res = 0

def dfs(level, change):
    global res
    if level == k:
        if change == t:
            res += 1
    elif change > t:
        return
    else:
        for i in range(0, coin[level][1]+1):
            dfs(level+1, change+i*coin[level][0])

dfs(0, 0)
print(res)