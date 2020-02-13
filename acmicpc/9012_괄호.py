import sys
input = lambda: sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    ps = input()
    # stack = list()
    stack = 0
    vps = True
    for p in ps:
        # print(f'p: {p}')
        if p == '(':
            # stack.append(p)
            stack += 1
        else:
            # if stack:
            #     del stack[-1]
            # else:
            #     vps = False
            #     break
            if stack > 0:
                stack -= 1
            else:
                vps = False
                break

        # print(f'stack: {stack}')
    if stack or not vps:
        print('NO')
    else:
        print('YES')