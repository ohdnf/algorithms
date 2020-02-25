import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    prog = list()
    incoming = list(map(int, input().split()))
    prog.extend(incoming)
    m -= 1
    while m > 0:
        incoming = list(map(int, input().split()))
        idx = -1
        for i in range(len(prog)):
            if prog[i] > incoming[0]:
                idx = i
                break
        if idx == -1:
            prog.extend(incoming)
        else:
            prog = prog[:idx] + incoming + prog[idx:]
            # prog.insert(idx, *incoming)
        m -= 1
    print('#{}'.format(test_case), end=' ')
    print(*prog[-1:-11:-1], sep=' ')
