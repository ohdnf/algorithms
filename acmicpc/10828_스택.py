import sys
input = lambda: sys.stdin.readline().rstrip()

res = list()
n = int(input())

for _ in range(n):
    cmd, *num = input().split()
    if cmd == 'push':
        res[len(res):] = [int(num[0])]
    elif cmd == 'pop':
        print(res.pop() if res else -1)
    elif cmd == 'size':
        print(len(res))
    elif cmd == 'empty':
        print(0 if res else 1)
    elif cmd == 'top':
        print(res[-1] if res else -1)
    # else:는 edge case들을 다 처리하기 때문에
    # 만약 test case 통과가 안 된다면
    # else 대신 elif로 처리하도록 하자