import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n > m:
        n, m = m, n
        a, b = b, a
    result = 0
    for i in range(m-n+1):
        temp = 0
        for j in range(n):
            temp += a[j] * b[j+i]
        if temp > result:
            result = temp
    print('#{0} {1}'.format(t, result))