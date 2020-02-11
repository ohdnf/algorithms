import sys
input = lambda: sys.stdin.readline()

n = int(input())
white = [[False for _ in range(101)] for _ in range(101)]
black = 0
for _ in range(n):
    r, c = map(int, input().split())
    for row in range(r, r+10):
        for col in range(c, c+10):
            if white[row][col]:
                pass
            else:
                black += 1
                white[row][col] = True
print(black)