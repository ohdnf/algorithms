import sys
sys.stdin = open('input.txt')

# def f(n, k):
#     global minV
#     if n == k:
#         s = 0
#         for i in range(k):
#             s += arr[i][p[i]]   # p[i]: i번 행에서 선택한 열 번호
#         if minV > s:
#             minV = s
#     else:
#         for i in range(k):
#             if u[i] == 0:
#                 u[i] = 1
#                 p[n] = i
#                 f(n+1, k)
#                 u[i] = 0

def f(n, k, s):
    global minV
    if n == k:
        if minV > s:
            minV = s
    elif minV <= s:
        return
    else:
        for i in range(k):
            if u[i] == 0:
                u[i] = 1
                f(n+1, k, s + arr[n][i])
                u[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    u = [0] * N
    p = [0] * N
    minV = 10 * N
    # f(0, N)
    f(0, N, 0)
    print('#{} {}'.format(tc, minV))