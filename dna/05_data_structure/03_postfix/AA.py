import sys
input = lambda: sys.stdin.readline()

sick = list(input().strip())
res = ''
stack = list()
# 연산 우선: (, )   >>>   *, /   >>>   +, -


for s in sick:
    if s.isdigit():
        res += s
    elif s == ')':
        while stack:
            if stack[-1] == '(':
                stack.pop()
                break
            else:
                res += stack.pop()
    elif s == '(':
        stack.append(s)
    elif s == '*' or s == '/':
        if not stack:
            stack.append(s)
        elif stack:
            if stack[-1] == '*' or stack[-1] == '/':
                res += stack.pop()
            stack.append(s)
    else:
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(s)

while stack:
    res += stack.pop()

print(res)
