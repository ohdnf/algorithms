import sys
input = lambda: sys.stdin.readline()

arr = list(input().strip())
stack = list()
pre = ''
result = 0
for curr in arr:
    if curr == '(':
        stack.append(curr)
    else:
        stack.pop()
        if pre == '(':
            result += len(stack)
        else:
            result += 1
    pre = curr
print(result)