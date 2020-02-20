import sys
sys.stdin = open('input.txt')

def get_min(i, k, s):
    global result
    if i == k:
        if s < result:
            result = s
    elif s >= result:
        return
    else:
        for j in range(k):
            if not check[j]:
                check[j] = True
                get_min(i+1, k, s+matrix[i][j])
                check[j] = False

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # N X N 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [0 for _ in range(N)]
    result = 9 * N
    get_min(0, N, 0)
    print('#{0} {1}'.format(test_case, result))
