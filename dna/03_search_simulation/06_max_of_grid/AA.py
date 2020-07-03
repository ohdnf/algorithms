import sys
input = lambda: sys.stdin.readline()


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
row = max([sum(line) for line in matrix])
col = max([sum(line) for line in list(zip(*matrix))])
diag = rev = 0
for i in range(n):
    diag += matrix[i][i]
    rev += matrix[i][n-i-1]

print(max(row, col, diag, rev))