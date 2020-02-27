import sys
sys.stdin = open('input.txt')

def calc(matrix, x, y, p, q):
    """
    시작 좌표(x, y)와 종료 좌표(p, q)로 화학 물질 컨테이너 크기(width * height) 계산
    """
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
    # 좌표 초기화
    r = c = x = y = p = q = 0
    containers = []

    while r < n:
        now = warehouse[r][c]
        if c:  # 첫번째 열 이후
            if warehouse[r][c-1]:   # 가로 길이 추가
                if now:
                    if c == n - 1:  # 마지막 열
                        q = c - 1
                        while warehouse[p][q]:  # 세로 길이 측정
                            p += 1
                            if p > n - 1:
                                break
                        p -= 1
                        warehouse, chemical = calc(warehouse, x, y, p, q)
                        containers.append(chemical)
                else:  # 가로 길이 종료
                    q = c - 1
                    while warehouse[p][q]:  # 세로 길이 측정
                        p += 1
                        if p > n - 1:
                            break
                    p -= 1
                    warehouse, chemical = calc(warehouse, x, y, p, q)
                    containers.append(chemical)
            else:
                if now:  # 가로 길이 시작
                    x, y = r, c
                    p = r
                else:
                    pass
        else:  # 첫번째 열
            if now:  # 화학 물질 ==> 가로 길이 시작
                x, y = r, c
                p = r
            else:   # 빈 용기
                pass
        c += 1
        if c > n - 1:
            c = 0
            r += 1
    # 크기가 작은 순으로, 크기가 같다면 행이 작은 순으로 정렬
    containers = sorted(containers, key=lambda c: (c[0]*c[1], c[0]))
    print('#{} {}'.format(test_case, len(containers)), end=' ')
    result = []
    for container in containers:
        result.extend(container)
    print(*result)