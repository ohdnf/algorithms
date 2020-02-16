import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    submit = set(map(int, input().split()))
    students = set(range(1, N+1))
    result = students - submit
    print('#{0} {1}'.format(test_case, ' '.join(map(str, result))))