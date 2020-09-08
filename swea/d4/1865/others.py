# 실행시간 3,310ms

def perm(k, temp=100):
    global max_val, n
    if k == n:
        if temp > max_val:
            max_val = temp
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            if temp * data[k][arr[k]] > max_val:  # 가지치기
                perm(k+1, temp*data[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]

for tc in range(1, int(input())+1):
    n = int(input())
    # arr = [ii for ii in range(n)]
    arr = list(range(n))
    data = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            data[i][j] *= 0.01
    max_val = 0
    perm(0)
    round(max_val, 7)
    print("#{} {}".format(tc, "%0.6f"%max_val))


# 실행시간 3,114ms

def toSet(num):
    return { idx for idx, val in enumerate(bin(num)[::-1]) if val == '1' }

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [ list(map(lambda x: int(x)/100, input().split())) for _ in range(N) ]
    
    ans = [0]*(1<<N)
    ans[0] = 1
    for n in range(N):
        for idx in range(1<<N):
            if ans[idx] == 0:
                if bin(idx).count('1') == n+1:
                    ans[idx] = max([ arr[n][i] * ans[idx & ~(1<<i)] for i in toSet(idx) ])
 
    print('#{} {:.6f}'.format(test, ans[-1]*100))