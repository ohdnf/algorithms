import sys, time
input = lambda: sys.stdin.readline()

start_time = time.time()

def combi(n, r):
    a = b = 1
    for j in range(n, n-r, -1):
        a *= j
    for k in range(r, 0, -1):
        b *= k
    return a // b

def dfs(level, nums):
    if level == l:
        cur = 0
        var = list(map(int, nums.split()))
        for i in range(l):
            cur += coef[i] * var[i]
        if cur == f:
            print(nums.lstrip())
            print(time.time() - start_time) # 3.689711809158325
            sys.exit(0)
    else:
        for num in range(1, l+1):
            if not chk[num]:
                chk[num] = True
                dfs(level+1, nums+' '+str(num))
                chk[num] = False

l, f = map(int, input().split())
chk = [False] * (l+1)
coef = [1] * l
for i in range(l):
    coef[i] *= combi(l-1, i)
# print(coef)


dfs(0, '')
