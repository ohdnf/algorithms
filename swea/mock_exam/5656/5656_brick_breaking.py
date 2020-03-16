import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n, h, w = map(int, input().split()) # swap w, h to use zip()
    data = [list(map(int, input().split())) for _ in range(w)]
    bricks = [list(line) for line in list(zip(*data))]

    print('#{}'.format(test_case))
