import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

n = int(input())
coin = [int(input()) for _ in range(n)]
res = float('inf')
def dfs(level, a, b, c):
    global res
    if level == n:
        if a != b and b != c and c != a:
            diff = max(a,b,c) - min(a,b,c)
            if res > diff:
                res = diff
    else:
        dfs(level+1, a+coin[level], b, c)
        dfs(level+1, a, b+coin[level], c)
        dfs(level+1, a, b, c+coin[level])

dfs(0, 0, 0, 0)
print(res)