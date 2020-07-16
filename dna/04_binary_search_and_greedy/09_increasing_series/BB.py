import sys
input = lambda: sys.stdin.readline()

n = int(input())
arr = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0
res = ''
tmp = list()

while lt <= rt:
    if arr[lt] > last:
        tmp.append((arr[lt], 'L'))
    if arr[rt] > last:
        tmp.append((arr[rt], 'R'))
    tmp.sort()
    if tmp:
        last = tmp[0][0]
        res += tmp[0][1]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    else:
        break
    tmp.clear()

print(len(res))
print(res)
        