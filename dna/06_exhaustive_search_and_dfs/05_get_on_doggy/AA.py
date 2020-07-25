import sys
input = lambda: sys.stdin.readline()

c, n = map(int, input().split())
dogs = [int(input()) for _ in range(n)]
res = 0

def dfs(idx, weights, notyet):
    """
    notyet = 앞으로 더해질 강아지들의 최대 무게
    weights = 지금까지 탑승한 강아지들의 무게
    """
    global res
    if idx == n:
        if weights == c:
            print(c)
            sys.exit(0)
        elif weights < c and weights > res:
            res = weights
        return
    # 가지치기 1
    elif weights + notyet < res:
        return
    # 가지치기 2
    elif weights >= c:
        return
    else:
        dfs(idx+1, weights+dogs[idx], notyet-dogs[idx])
        dfs(idx+1, weights, notyet-dogs[idx])

dfs(0, 0, sum(dogs))

print(res)