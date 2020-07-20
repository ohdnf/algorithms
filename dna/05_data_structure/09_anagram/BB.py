import sys
input = lambda: sys.stdin.readline()

first = input().strip()
second = input().strip()

d = dict()
for c in first:
    d[c] = d.get(c, 0) + 1

for c in second:
    d[c] = d.get(c, 0) - 1

for v in d.values():
    if v != 0:
        print('NO')
        break
else:
    print('YES')
