import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    max_route = 0
    print('#{} {}'.format(test_case, max_route))