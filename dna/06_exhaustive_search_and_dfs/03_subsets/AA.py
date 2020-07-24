import sys
input = lambda: sys.stdin.readline()

n = int(input())
chk = [False] * (n+1)

def dfs(idx, last):
    if idx > last:
        for num in range(1, n+1):
            if chk[num]:
                print(num, end=' ')
        print()
    else:
        chk[idx] = True
        dfs(idx+1, last)
        chk[idx] = False
        dfs(idx+1, last)

dfs(1, n)
