import sys
input = lambda: sys.stdin.readline()

first = dict()
for c in input().strip():
    # if c in first:
    #     first[c] += 1
    # else:
    #     first[c] = 1
    first[c] = first.get(c, 0) + 1

second = dict()
for c in input().strip():
    second[c] = second.get(c, 0) + 1

if first == second:
    print('YES')
else:
    print('NO')