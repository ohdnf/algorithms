import sys
sys.stdin = open('input.txt')

def search(target, left, right, direction):
    idx = (left + right) // 2
    mid = A[idx]
    if target == mid:
        return 1
    elif target < mid and direction != 'l':
        return search(target, left, idx-1, 'l')
    elif target > mid and direction != 'r':
        return search(target, idx+1, right, 'r')
    else:
        return 0

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    result = 0
    for num in B:
        result += search(num, 0, len(A)-1, '')
    print('#{} {}'.format(test_case, result))