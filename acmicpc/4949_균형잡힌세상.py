import sys
input = lambda: sys.stdin.readline().rstrip()

world = ''
finished = False
while world != '.' and not finished:
    world = input()
    if world == '.':
        finished = True
    else:
        stack = []
        for s in world:
            if s == '[' or s == '(':
                stack.append(s)
            elif s == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        print('no')
                        break
                else:
                    print('no')
                    break
            elif s == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        print('no')
                        break
                else:
                    print('no')
                    break
        else:
            if stack:
                print('no')
            else:
                print('yes')