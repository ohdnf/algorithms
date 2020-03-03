import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    ret = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and D[x][y] + 1 == D[nx][ny]:
            ret += DFS(nx, ny)
    return ret
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    m = 0
    r = float('inf')
    for i in range(N):
        for j in range(N):
            s = DFS(i,j)
            if s > m:
                m = s
                r = D[i][j]
            elif s == m:
                r = min(r,D[i][j])
    print('#{} {} {}'.format(tc, r, m))