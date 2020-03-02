import sys
sys.stdin = open('input.txt')

def f(n, s, d, m, m3):
    global minV
    if n > 12:
        if minV > s:
            minV = s
    elif minV <= s:
        return
    else:
        f(n+1, s+min(table[n]*d, m), d, m, m3)
        f(n+3, s+m3, d, m, m3)

t = int(input())
for test_case in range(1, t+1):
    d, m, m3, y = map(int, input().split())
    table = [0] + list(map(int, input().split()))
    minV = y
    f(1, 0, d, m, m3)
    print('#{} {}'.format(test_case, minV))