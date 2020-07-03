import sys
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i, n):
        if sum(arr[i:j+1]) == m:
            res += 1
print(res)