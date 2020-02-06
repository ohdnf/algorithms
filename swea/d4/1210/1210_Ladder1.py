for _ in range(1, 11):
    case = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    line = ladders[99].index(2)
    for step in range(98, 0, -1):
        cur = line
        if line > 0 and ladders[step][line-1] == 1:
            while cur > 0 and ladders[step][cur-1] == 1:
                cur -= 1
        elif line < 99 and ladders[step][line+1] == 1:
            while cur < 99 and ladders[step][cur+1] == 1:
                cur += 1
        line = cur
    print('#{} {}'.format(case, line))
        
# 0. bottom-up 방식  
# 1. 시작지점 설정
# 2. 위로 한 칸 올라와서 양옆 체크
# 2-0. 양 옆에 0 없으면 위로 이동
# 2-1. 왼쪽 x > -1 이고 x == 1일 때까지 왼쪽으로 이동(x++)
# 2-2. 오른쪽 x < 100 이고 x == 1일 때까지 오른쪽으로 이동(x--)
# 3. y == 0일 때까지 2 반복