import sys
sys.stdin = open('input.txt')

icp = {'(': 3, '+': 1, '*': 2}
isp = {'(': 0, '+': 1, '*': 2}

for test_case in range(1, 11):
    length = int(input())
    sick = input().strip()
    stack = list()
    expression = ''
    for token in sick:
        if token.isdigit():
            expression += token
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                expression += stack.pop()
            stack.pop()
        else:
            while stack and icp[token] <= isp[stack[-1]]:
                expression += stack.pop()
            stack.append(token)
    while stack:
        expression += stack.pop()
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token == '+':
            second = stack.pop()
            first = stack.pop()
            stack.append(first+second)
        elif token == '*':
            second = stack.pop()
            first = stack.pop()
            stack.append(first*second)
    print('#{} {}'.format(test_case, stack[-1]))