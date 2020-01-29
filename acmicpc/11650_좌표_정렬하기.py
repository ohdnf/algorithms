import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

coordinates = [list(map(int, input().split())) for _ in range(N)]

result = sorted(coordinates, key=lambda c: (c[0], c[1]))

for x, y in result:
    print(x, y)