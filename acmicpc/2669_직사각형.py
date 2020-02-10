import sys
input = lambda: sys.stdin.readline().rstrip()

area = [[0 for _ in range(100)] for _ in range(100)]
result = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(y1-1, y2-1):
        for col in range(x1-1, x2-1):
            if area[row][col]:
                pass
            else:
                area[row][col] += 1
                result += 1
print(result)