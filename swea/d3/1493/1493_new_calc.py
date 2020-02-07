import sys
sys.stdin = open('input.txt')

def sharp(x, y):
    # (대각선 번호) = (x좌표) + (y좌표) - 1
    # (y좌표) = (대각선 번호) - (x좌표) + 1
    cardinal = x + y - 1
    return sum(range(cardinal)) + x

def ampersand(number):
    cardinal = 0
    while True:
        cardinal += 1   # 현재 대각선 번호
        last = sum(range(cardinal+1))  # 현재 대각선의 마지막 숫자
        if last == number:
            return cardinal, 1
        elif last > number:
            return cardinal - last + number, last - number + 1

T = int(input())
for t in range(1, T+1):
    p, q = map(int, input().split())
    px, py = ampersand(p)
    qx, qy = ampersand(q)
    result = sharp(px+qx, py+qy)
    print('#{0} {1}'.format(t, result))

    