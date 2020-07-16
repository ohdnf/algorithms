from collections import deque
import sys
input = lambda: sys.stdin.readline()

number, m = input().split()

number = deque(map(int, list(number)))
m = int(m)
res = deque()

while number and m:
    curr = number.popleft()
    while res and m and res[-1] < curr:
        res.pop()
        m -= 1
    res.append(curr)
res.extend(number)
while res and m:
    res.pop()
    m -= 1
print(*res, sep='')