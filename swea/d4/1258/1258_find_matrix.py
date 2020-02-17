import sys
sys.stdin = open('input.txt')

def calc(matrix, x, y, p, q):
    height = p - x + 1
    width = q - y + 1
    for i in range(x, p+1):
        for j in range(y, q+1):
            matrix[i][j] = 0
    return matrix, [height, width]

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(n)]

    r = c = x = y = p = q = 0
    containers = []

    while r < n:
        now = warehouse[r][c]
        if c:  # after first column
            if warehouse[r][c-1]:
                if now:  # width continue
                    if c == n - 1:  # width stop
                        q = c - 1
                        while warehouse[p][q]:
                            p += 1
                            if p > n - 1:
                                break
                        p -= 1
                        warehouse, chemical = calc(warehouse, x, y, p, q)
                        containers.append(chemical)
                else:  # width stop
                    q = c - 1
                    while warehouse[p][q]:
                        p += 1
                        if p > n - 1:
                            break
                    p -= 1
                    warehouse, chemical = calc(warehouse, x, y, p, q)
                    containers.append(chemical)
            else:
                if now:  # width start
                    x, y = r, c
                    p = r
                else:
                    pass
        else:  # first column
            if now:  # width start
                x, y = r, c
                p = r
            else:
                pass
        c += 1
        if c > n - 1:
            c = 0
            r += 1
    
    containers = sorted(containers, key=lambda c: (c[0]*c[1], c[0]))
    print('#{} {}'.format(test_case, len(containers)), end=' ')
    result = []
    for container in containers:
        result.extend(container)
    print(*result)