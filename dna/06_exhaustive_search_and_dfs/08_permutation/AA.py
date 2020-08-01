import sys
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
chk = [False] * (n+1)
res = 0
def dfs(depth, beads):
    global res
    if depth == m:
        res += 1
        print(' '.join(list(beads)))
    else:
        for num in range(1, n+1):
            if not chk[num]:
                chk[num] = True
                dfs(depth+1, beads+str(num))
                chk[num] = False

dfs(0, '')
print(res)