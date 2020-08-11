import sys
input = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open('in1.txt')

n = int(input())
time = [0] * n
profit = [0] * n
for idx in range(n):
    time[idx], profit[idx] = map(int, input().split())

res = 0

def dfs(day, earned):
    global res
    if day > n:
        return
    if day == n:
        if res < earned:
            res = earned

    else:
        dfs(day+time[day], earned+profit[day])
        dfs(day+1, earned)

dfs(0, 0)
print(res)