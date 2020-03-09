import sys
sys.stdin = open('input.txt')

def dfs(x, y, max_row, max_col, hour, limit):
    if hour == limit:
        return
    else:
        check[x][y] = 1
        locations.add((x, y))
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + dx
            ny = y + dy
            if 0<=nx<max_row and 0<=ny<max_col and check[nx][ny] == 0:
                # up
                if dx == -1 and dy == 0 and tunnel[x][y] in (1, 2, 4, 7) and tunnel[nx][ny] in (1, 2, 5, 6):
                    dfs(nx, ny, max_row, max_col, hour+1, limit)
                # down
                elif dx == 1 and dy == 0 and tunnel[x][y] in (1, 2, 5, 6) and tunnel[nx][ny] in (1, 2, 4, 7):
                    dfs(nx, ny, max_row, max_col, hour+1, limit)
                # left
                elif dx == 0 and dy == -1 and tunnel[x][y] in (1, 3, 6, 7) and tunnel[nx][ny] in (1, 3, 4, 5):
                    dfs(nx, ny, max_row, max_col, hour+1, limit)
                # right
                elif dx == 0 and dy == 1 and tunnel[x][y] in (1, 3, 4, 5) and tunnel[nx][ny] in (1, 3, 6, 7):
                    dfs(nx, ny, max_row, max_col, hour+1, limit)
        check[x][y] = 0

t = int(input())
for test_case in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    check = [[0 for _ in range(m)] for _ in range(n)]
    locations = set()
    dfs(r, c, n, m, 0, l)
    print('#{} {}'.format(test_case, len(locations)))