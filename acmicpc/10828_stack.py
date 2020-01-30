import sys
input = lambda: sys.stdin.readline().rstrip()

res = list()
n = int(input())

for _ in range(n):
    cmd, *num = input().split()
    if cmd == 'push':
        res[len(res):] = [int(num[0])]
    elif cmd == 'pop':
        print(res.pop() if any(res) else -1)
    elif cmd == 'size':
        print(len(res))
    elif cmd == 'empty':
        print(0 if any(res) else 1)
    elif cmd == 'top':
        print(res[-1] if any(res) else -1)