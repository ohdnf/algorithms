import sys
input = lambda: sys.stdin.readline().rstrip()

res = list()
n = int(input())
for _ in range(n):
    cmd, *num = input().split()
    if cmd == 'push_front':
        res = [int(num[0])] + res
    elif cmd == 'push_back':
        res += [int(num[0])]
    elif cmd == 'pop_front':
        print(res.pop(0) if any(res) else -1)
    elif cmd == 'pop_back':
        print(res.pop() if any(res) else -1)
    elif cmd == 'size':
        print(len(res))
    elif cmd == 'empty':
        print(0 if any(res) else 1)
    elif cmd == 'front':
        print(res[0] if any(res) else -1)
    elif cmd == 'back':
        print(res[-1] if any(res) else -1)
