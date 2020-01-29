import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

coords = sorted(coords, key=lambda c: (c[1], c[0]))
for x, y in coords:
    print(x, y)