dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x,y,v):
    global Possible
    if v == N-1:
        Possible = 1
        return
     
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < M:
            if not check[nx][ny] and D[nx][ny] == A[v+1]:
                check[nx][ny] = 1
                DFS(nx,ny,v+1)
                check[nx][ny] = 0
 
T = int(input())
for tc in range(1, T+1):
    N, *A = map(int, input().split())
    M = int(input())
    D = [list(map(int,input().split())) for _ in range(M)]
    check = [[0]*M for _ in range(M)]
    Possible = 0
    axis = [[i,j] for i in range(M) for j in range(M) if D[i][j] == A[0]]
    for a in axis:
        c, r = a
        if Possible:
            break
        else:
            DFS(c,r,0)
    print('#{} {}'.format(tc,Possible))