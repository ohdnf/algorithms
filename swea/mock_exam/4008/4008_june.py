# a, b = -3, 2
# print(a//b)
# print(int(a/b))
# if a < 0:
#     print(-(abs(a)//b))
# else:
#     print(a//b)

def f(n, k, r, op1, op2, op3, op4):
    global minV, maxV
    if n == k:
        if maxV < r:
            maxV = r
        if minV > r:
            minV = r
    else:
        if op1 > 0:
            f(n+1, k, r+card[n], op1-1, op2, op3, op4)
        if op2 > 0:
            f(n+1, k, r-card[n], op1, op2-1, op3, op4)
        if op3 > 0:
            f(n+1, k, r*card[n], op1, op2, op3-1, op4)
        if op4 > 0:
            f(n+1, k, int(r/card[n]), op1, op2, op3, op4-1)

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    card = list(map(int, input().split()))
    minV = 10000000000
    maxV = -10000000000
    f(1, n, card[0], op1, op2, op3, op4)
    print('#{} {}',format(test_case, maxV-minV))