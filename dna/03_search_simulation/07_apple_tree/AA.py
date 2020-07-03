import sys
input = lambda: sys.stdin.readline()

n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]

center = n // 2
i = res = 0
for j in range(n):
    res += sum(farm[j][center-i:center+i+1])
    if j < center:
        i += 1
    else:
        i -= 1
print(res)