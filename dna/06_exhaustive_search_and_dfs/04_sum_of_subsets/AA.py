import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
g = list(map(int, input().split()))
chk = {num: False for num in g}
flag = False

# def dfs(idx):
#     global flag
#     if idx == n:
#         lt = sum([l for l in g if chk[l]])
#         rt = sum([r for r in g if not chk[r]])
#         if lt == rt:
#             flag = True
#     else:
#         num = g[idx]
#         chk[num] = True
#         dfs(idx+1)
#         chk[num] = False
#         dfs(idx+1)

def dfs(idx, g1, g2):
    global flag
    if idx == n:
        if g1 == g2:
            flag = True
    else:
        dfs(idx+1, g1+g[idx], g2)
        dfs(idx+1, g1, g2+g[idx])

dfs(0, 0, 0)

if flag:
    print('YES')
else:
    print('NO')