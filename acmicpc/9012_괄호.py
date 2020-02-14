import sys
input = lambda: sys.stdin.readline().strip()
# input = lambda: sys.stdin.readline()
# 위와 같이 입력하면 문자열 맨 끝에 줄바꿈(\n) 문자가 추가된다.

t = int(input())
for _ in range(t):
    ps = input()
    stack = 0
    for p in ps:
        if p == '(':
            stack += 1
        else:
            if stack > 0:
                stack -= 1
            else:
                print('NO')
                break
    # for문에서 break를 안 만나면 else문 실행
    else:
        if stack:
            print('NO')
        else:
            print('YES')