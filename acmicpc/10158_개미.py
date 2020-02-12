import sys
input = lambda: sys.stdin.readline()

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x = t // w
y = t // h
if x % 2:
    pass
else:
    p = w-p
if y % 2:
    pass
else:
    q = h-q
print(p, q)
