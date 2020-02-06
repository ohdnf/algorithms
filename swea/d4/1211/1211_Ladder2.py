for _ in range(1, 11):
    case = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    starts = [i for i, d in enumerate(ladders[99]) if d]
    distances = []
    for start in starts:
        line = start
        move = 0
        for step in range(98, 0, -1):
            cur = line
            move += 1
            if line > 0 and ladders[step][line-1] == 1:
                while cur > 0 and ladders[step][cur-1] == 1:
                    cur -= 1
                    move += 1
            elif line < 99 and ladders[step][line+1] == 1:
                while cur < 99 and ladders[step][cur+1] == 1:
                    cur += 1
                    move += 1
            line = cur
        distances.append([line, move])
    result = sorted(distances, key=lambda d: d[1])
    print('#{} {}'.format(case, result[0][0]))