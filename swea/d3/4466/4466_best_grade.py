import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    scores = sorted(list(map(int, input().split())), reverse=True)
    result = sum(scores[:k])
    print('#{} {}'.format(test_case, result))