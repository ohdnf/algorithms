import sys
input = lambda: sys.stdin.readline()
# sys.stdin = open('in1.txt')

n, m = map(int, input().split())
point = list()
time = list()
for _ in range(n):
    p, t = map(int, input().split())
    point.append(p)
    time.append(t)

res = 0

def dfs(num, elapsed, total):
    global res
    if elapsed > m:
        return
    if num == n:
        if res < total:
            res = total
    else:
        dfs(num+1, elapsed+time[num], total+point[num])
        dfs(num+1, elapsed, total)


dfs(0, 0, 0)
print(res)