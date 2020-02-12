import sys
input = lambda: sys.stdin.readline()

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x, y = 1, 1
p += x
q += y
# 천장
if q == h:
    y = -1
# 바닥
if q == 0:
    y = 1
# 왼쪽
if p == 0:
    x = 1
# 오른쪽
if p == w:
    x = -1
print(p, q)
