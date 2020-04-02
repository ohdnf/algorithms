import sys
sys.stdin = open('input.txt')

def dfs(x, y, route):
    global max_route
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and area[nx][ny] < area[x][y]:
            dfs(nx, ny, route+1)
    else:
        if route > max_route:
            max_route = route

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    max_route = 0

    # 가장 높은 봉우리(==시작점) 찾기
    peaks = list()
    max_peak = 0
    for r in range(n):
        for c in range(n):
            curr = area[r][c]
            if curr > max_peak:
                max_peak = curr
                peaks = [(r, c)]
            elif curr == max_peak:
                peaks.append((r, c))
    
    # 공사 다 해보기
    for row in range(n):
        for col in range(n):
            orig = area[row][col]
            for depth in range(k+1):
                # 공사깊이가 지형높이보다 커지면 pass
                if orig < depth:
                    break
                area[row][col] -= depth # 공사하기

                # 등산로 찾기
                for px, py in peaks:
                    visited = [[False]*n for _ in range(n)]
                    dfs(px, py, 1)

                    # 스택 이용
                    # q = [(px, py, 1)]
                    # while q:
                    #     x, y, route = q.pop()
                    #     visited[x][y] = True
                    #     for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    #         nx = x + dx
                    #         ny = y + dy
                    #         if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                    #             if area[nx][ny] < area[x][y]:
                    #                 q.append((nx, ny, route+1))
                    #    if route > max_route:
                    #        max_route = route
                
                area[row][col] = orig   # 복원하기
    print('#{} {}'.format(test_case, max_route))