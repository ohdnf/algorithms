from collections import deque
import sys, copy
input = lambda: sys.stdin.readline()

required = input()
n = int(input())
for case in range(1, n+1):
    req = deque(required)
    curr = input()
    for sub in curr:
        if sub in req:
            if sub != req.popleft():
                print(f"#{case} NO")
                break
    else:
        if req:
            print(f"#{case} NO")
        else:
            print(f"#{case} YES")

    