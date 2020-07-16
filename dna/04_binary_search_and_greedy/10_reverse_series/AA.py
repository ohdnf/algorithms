import sys
input = lambda: sys.stdin.readline()

n = int(input())
rev = list(map(int, input().split()))

orig = [0] * n

for i, big in enumerate(rev):
    num = i + 1
    idx = cnt = 0
    while cnt < big:
        if orig[idx] == 0:
            cnt += 1
        idx += 1
    while orig[idx]:
        idx += 1
    orig[idx] = num
    # print(num, orig)

print(*orig, sep=' ')
