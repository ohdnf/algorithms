import sys
input = lambda: sys.stdin.readline().rstrip()

k = int(input())
weight = list(map(int, input().split()))
mx = sum(weight)
water = [0] * (mx+1)

# def dfs(level, curr):
#     if level == k:
#         water[curr] = 1
#         water[mx-curr] = 1
#     else:
#         dfs(level+1, curr+weight[level])
#         dfs(level+1, curr)

def dfs(level, left, right):
    if level == k:
        water[left] = 1
        # water[right] = 1  // left와 대칭된 값
        water[abs(left-right)] = 1
    else:
        dfs(level+1, left+weight[level], right)
        dfs(level+1, left, right+weight[level])
        dfs(level+1, left, right)

dfs(0, 0, 0)
print(water.count(0))