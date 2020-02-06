T = int(input())
for t in range(1, T+1):
    matrix = [[0]*10 for _ in range(10)]
    n = int(input())
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        r1, r2 = min(r1, r2), max(r1, r2)
        c1, c2 = min(c1, c2), max(c1, c2)
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                matrix[x][y] += color
    
    violet = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                violet += 1
    
    print('#{0} {1}'.format(t, violet))