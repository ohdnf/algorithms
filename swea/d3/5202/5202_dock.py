import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    incomings = list()
    for _ in range(n):
        s, e = map(int, input().split())
        incomings.append([s, e])
    result = 0
    print(incomings)
    print('#{} {}'.format(test_case, result))