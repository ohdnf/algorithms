import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n, m, l = map(int, input().split())
    prog = list(map(int, input().split()))
    for _ in range(m):
        idx, num = map(int, input().split())
        prog.insert(idx, num)
    print('#{} {}'.format(test_case, prog[l]))