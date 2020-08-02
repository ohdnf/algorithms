import sys, time
input = lambda: sys.stdin.readline().rstrip()

start_time = time.time()

n, f = map(int, input().split())

# 파스칼 삼각형 이항계수
coef = [1] * n
for i in range(1, n):
    coef[i] = coef[i-1] * (n-i) // i
# print(coef)

nums = [0] * n
chk = [False] * (n + 1)

# DFS
def dfs(level, hap):
    if level == n and hap == f:
        print(*nums)
        print(time.time() - start_time) # 3.0619678497314453
        sys.exit(0)
    else:
        for num in range(1, n+1):
            if not chk[num]:
                chk[num] = True
                nums[level] = num
                dfs(level+1, hap+coef[level] * nums[level])
                chk[num] = False

dfs(0, 0)