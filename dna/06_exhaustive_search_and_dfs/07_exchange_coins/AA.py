import sys
input = lambda: sys.stdin.readline()

n = int(input())
coins = sorted(list(map(int, input().split())), reverse=True)
m = int(input())

# 이 코드는 최적해를 찾을 수 없음
# cnt = 0
# for coin in coins:
#     if m <= 0:
#         break
#     change = m // coin
#     cnt += change
#     m -= change * coin
# print(cnt)

# 1차 코드: 통과
# res = 500
# def dfs(idx, remain, cnt):
#     global res
#     if idx == n:
#         if remain == 0 and res > cnt:
#             res = cnt
#     elif cnt >= res:
#         return
#     else:
#         curr = coins[idx]
#         for c in range(remain//curr, -1, -1):
#             dfs(idx+1, remain-curr*c, cnt+c)
# dfs(0, m, 0)
# print(res)

# 2차 코드
res = 500
def dfs(cnt, change):
    global res
    if change == m and res > cnt:
        res = cnt
    elif change > m or res <= cnt:
        return
    else:
        for coin in coins:
            dfs(cnt+1, change+coin)
dfs(0, 0)
print(res)
