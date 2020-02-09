import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    carrots = [list(map(int, input().split())) for _ in range(n)]
    section = [0, 0, 0, 0]
    for row in range(n):
        for col in range(n):
            if row < col and (n-row-1) > col:
                section[0] += carrots[row][col]
            elif row < col and (n-row-1) < col:
                section[1] += carrots[row][col]
            elif row > col and (n-row-1) < col:
                section[2] += carrots[row][col]
            elif row > col and (n-row-1) > col:
                section[3] += carrots[row][col]
    mx = mn = section[0]
    for i in range(1, 4):
        sec = section[i]
        if sec > mx:
            mx = sec
        if sec < mn:
            mn = sec
    print('#{0} {1}'.format(t, mx-mn))
