import sys
input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
nums = list(map(int, input().split()))
m = int(input())

tmp = [0] * k
chk = {num: False for num in nums}
res = 0

def dfs(level, total, start):
# def dfs(level, start):
    global res
    if level == k:
        if total % m == 0:
            res += 1
        # if sum(tmp) % m == 0:
        #     res += 1
    else:
        for idx in range(start, n):
            if not chk[nums[idx]]:
                chk[nums[idx]] = True
                tmp[level] = nums[idx]
                dfs(level+1, total+nums[idx], idx+1)
                # dfs(level+1, idx+1)
                chk[nums[idx]] = False

dfs(0, 0, 0)
# dfs(0, 0)

print(res)
