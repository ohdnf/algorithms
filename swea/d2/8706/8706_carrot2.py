import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    carrots = [0] + list(map(int, input().split()))
    cart = 0
    distance = 0
    for i in range(1, n+1):
        cart += carrots[i]
        distance += 1
        while cart >= m:
            cart -= m
            distance += i*2
    distance += n
    print('#{0} {1}'.format(t, distance))