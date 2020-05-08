import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, 1+t):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    result = 0
    w.sort()
    t.sort()
    while w:
        container_now = w.pop()
        for idx, capacity in enumerate(t):
            if capacity >= container_now:
                result += container_now
                t.pop(idx)
                break
    print('#{} {}'.format(test_case, result))