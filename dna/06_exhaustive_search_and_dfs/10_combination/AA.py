import sys
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())

chk = [False] * (n+1)
res = [0] * m
cnt = 0

def dfs(level, start):
    global cnt
    if level == m:
        print(*res)
        cnt += 1
    else:
        for num in range(start, n+1):
            if not chk[num]:
                chk[num] = True
                res[level] = num
                dfs(level+1, num+1)
                chk[num] = False

dfs(0, 1)
print(cnt)
