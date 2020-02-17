import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda: sys.stdout.write()

n = int(input())
result = [int(input()) for _ in range(n)]
result.reverse()

#         4 3     6     8 7 5 2 1
# 1 2 3 4 4 3 5 6 6 7 8 8 7 5 2 1
# + + + + - - + + - + + - - - - -

number = 1
no = False
operands = []
stack = []
while (number <= n or result) and not no:
    if stack:
        if result[-1] > stack[-1]:
            stack.append(number)
            number += 1
            operands.append('+')
        elif result[-1] == stack[-1]:
            result.pop()
            stack.pop()
            operands.append('-')
        elif result[-1] < stack[-1]:
            no = True
    else:
        stack.append(number)
        number += 1
        operands.append('+')

if no:
    print('NO')
else:
    print(*operands, sep='\n')
