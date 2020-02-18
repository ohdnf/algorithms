import sys
input = lambda: sys.stdin.readline().rstrip()

string = list(input())
m = int(input())
stack = []
for _ in range(m):
    cmd, *char = input().split()
    if cmd == 'L':
        if string:
            stack.append(string.pop())
        else:
            pass
    elif cmd == 'D':
        if stack:
            string.append(stack.pop())
        else:
            pass
    elif cmd == 'B':
        if string:
            string.pop()
        else:
            pass
    elif cmd == 'P':
        string.append(char[0])
    # print(string, stack)

string += reversed(stack)
print(*string, sep='')
