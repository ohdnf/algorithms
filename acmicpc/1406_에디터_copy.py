import sys
input = lambda: sys.stdin.readline().rstrip()

string = input()
last = cursor = len(string) - 1
string = string
m = int(input())

# -1 : 맨 앞

for _ in range(m):
    cmd, *char = input().split()
    if cmd == 'L':
        if cursor >= 0:
            cursor -= 1
    elif cmd == 'D':
        if cursor < last:
            cursor += 1
    elif cmd == 'B':
        if cursor == 0:
            string = string[1:]
        elif cursor == last:
            string = string[:cursor]
            cursor -= 1
            last -= 1
        elif cursor > 0:
            string = string[:cursor] + string[cursor+1:]
            cursor -= 1
            last -= 1
    elif cmd == 'P':
        if cursor == -1:
            string = char[0] + string
            cursor += 1
        elif cursor == last:
            string = string + char[0]
            cursor += 1
        elif cursor > -1 and cursor < last:
            string = string[:cursor+1] + char[0] + string[cursor+1:]
        last += 1

sys.stdout.write(string)