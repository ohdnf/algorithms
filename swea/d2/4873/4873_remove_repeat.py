import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    s = list(input())
    stack = list()
    while s:
        stack.append(s.pop(0))
        while stack and s and stack[-1] == s[0]:
            stack.pop()
            s.pop(0)
    print(stack)
    print('#{} {}'.format(t, len(stack)))