import sys
input = lambda: sys.stdin.readline()

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p += t
q += t

if (p // w) % 2:
    x = w - p % w
else:
    x = p % w

if (q // h) % 2:
    y = h - q % h
else:
    y = q % h

print(x, y)