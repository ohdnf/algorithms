import sys
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
result = 0
def dfs(depth, nums):
    global result
    if depth > m:
        print(' '.join(list(nums)))
        result += 1
    else:
        for num in range(1, n+1):
            dfs(depth+1, nums+str(num))

dfs(1, '')

print(result)