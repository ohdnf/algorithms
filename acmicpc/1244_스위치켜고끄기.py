import sys

input = lambda: sys.stdin.readline().rstrip()

def change(switch):
    return 0 if switch else 1

n = int(input())
sw = [0] + list(map(int, input().split()))

st = int(input())
for _ in range(st):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, n+1, num):
            sw[i] = change(sw[i])

    elif gender == 2:
        sw[num] = change(sw[num])
        i = 1
        while num - i > 0 and num + i <= n:
            if sw[num-i] == sw[num+i]:
                sw[num-i] = change(sw[num-i])
                sw[num+i] = change(sw[num+i])
            else:
                break
            i += 1

del sw[0]

for i, s in enumerate(sw, start=1):
    if i % 20:
        print(s, end=' ')
    else:
        print(s)
