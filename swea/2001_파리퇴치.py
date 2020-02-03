T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]

    most_kill = 0
    # 파리채의 x 좌표
    for i in range(n-m+1):
        # 파리채의 y 좌표
        for j in range(n-m+1):
            # 죽은 파리의 개수
            kill = 0
            for k in range(m):
                for f in flies[i+k][j:j+m]:
                    kill += f
            # 최댓값 비교
            if kill > most_kill:
                most_kill = kill
    print('#{0} {1}'.format(t, most_kill))