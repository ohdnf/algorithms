from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

string = deque(input())
last = cursor = len(string)
m = int(input())

for _ in range(m):
    cmd, *char = input().split()
    if cmd == 'L':
        pass
    elif cmd == 'D':
        pass
    elif cmd == 'B':
        pass
    elif cmd == 'P':
        pass

sys.stdout.write(string)