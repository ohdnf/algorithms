import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    warehouse = [list(map(int, input())) for _ in range(n)]

    print('#{}'.format(test_case))