import sys
input = lambda: sys.stdin.readline()

arr = list(input().strip())
stack = list()
pre = ''
result = 0
for curr in arr:
    if curr == '(':
        stack.append(curr)
        pre = curr
    else:
        if pre == '(':
            stack.pop() # 레이저 괄호 제거
            result += len(stack)
        else:
            stack.pop()
            result += 1
        pre = ')'
print(result)