from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')
# sys.stdin = open('dna/07_dfs_and_bfs/12_numbering_complex/in1.txt')


n = int(input())
town = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

d = ((0, 1), (1, 0), (0, -1), (-1, 0))
number = 1
cmplx = list()

for row in range(n):
    for col in range(n):
        if town[row][col] and not visited[row][col]:
            search = dq()
            search.append((row, col))
            town[row][col] = number
            visited[row][col] = True
            cnt = 1
            while search:
                crow, ccol = search.popleft()
                for drow, dcol in d:
                    nrow, ncol = crow+drow, ccol+dcol
                    if 0<=nrow<n and 0<=ncol<n and town[nrow][ncol] and not visited[nrow][ncol]:
                        cnt += 1
                        town[nrow][ncol] = number
                        visited[nrow][ncol] = True
                        search.append((nrow, ncol))
            cmplx.append(cnt)
            number += 1

cmplx.sort()
print(len(cmplx))
for houses in cmplx:
    print(houses)

def dfs(row, col):
    return