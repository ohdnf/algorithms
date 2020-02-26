import sys
sys.stdin = open('input.txt')
import time

start_time = time.time()

from collections import deque

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    prog = deque()
    incoming = deque(map(int, input().split()))
    prog.extend(incoming)
    m -= 1
    while m > 0:
        incoming = deque(map(int, input().split()))
        idx = -1
        for i in range(len(prog)):
            if prog[i] > incoming[0]:
                idx = i
                break
        if idx == 0:
            prog.extendleft(incoming)
        elif idx == -1:
            prog.extend(incoming)
        else:
            for i in range(n-1, -1, -1):
                prog.insert(idx, incoming[i])
        m -= 1
    result = ''
    for _ in range(10):
        result += ' ' + str(prog.pop())
    print('#{}{}'.format(test_case, result))

print(time.time() - start_time)