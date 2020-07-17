import sys
input = lambda: sys.stdin.readline()

post = list(input().strip())
stack = list()
for p in post:
    if p.isdigit():
        stack.append(int(p))
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if p == '+':
            stack.append(n1+n2)
        elif p == '-':
            stack.append(n1-n2)
        elif p == '*':
            stack.append(n1*n2)
        elif p == '/':
            stack.append(n1/n2)

print(stack[-1])