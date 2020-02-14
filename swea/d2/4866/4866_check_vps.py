import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    string = input().strip()
    stack = list()
    good = 1
    for s in string:
        if s == '{' or s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack.pop() == '(':
                    pass
                else:
                    good = 0
                    break
            else:
                good = 0
                break
        elif s == '}':
            if stack:
                if stack.pop() == '{':
                    pass
                else:
                    good = 0
                    break
            else:
                good = 0
                break
    if stack:
        good = 0
    print('#{0} {1}'.format(t, good))
     