import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in2.txt')

n = int(input())
start = (-1, -1, float('inf'))
end = (-1, -1, 0)
mt = list()
for row in range(n):
    line = list(map(int, input().split()))
    mt.append(line)
    for col in range(n):
        if line[col] < start[2]:
            start = (row, col, line[col])
        if line[col] > end[2]:
            end = (row, col, line[col])

# print('start:', start)
# print('end:', end)      

visited = [[False]*n for _ in range(n)]

d = ((0, 1), (1, 0), (0, -1), (-1, 0))
res = 0

def dfs(row, col):
    global res
    if row == end[0] and col == end[1]:
        res += 1
    else:
        for drow, dcol in d:
            nrow, ncol = row+drow, col+dcol
            if 0<=nrow<n and 0<=ncol<n and not visited[nrow][ncol] and mt[nrow][ncol] > mt[row][col]:
                visited[nrow][ncol] = True
                dfs(nrow, ncol)
                visited[nrow][ncol] = False

visited[start[0]][start[1]] = True
dfs(start[0], start[1])
print(res)
