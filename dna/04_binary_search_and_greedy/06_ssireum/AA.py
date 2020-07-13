import sys
input = lambda: sys.stdin.readline()

n = int(input())

candidates = [list(map(int, input().split())) for _ in range(n)]
candidates.sort(reverse=True)

max_w = cnt = 0
for h, w in candidates:
    if w > max_w:
        max_w = w
        cnt += 1

print(cnt)