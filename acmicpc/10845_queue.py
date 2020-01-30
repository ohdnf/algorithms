import sys
input = lambda: sys.stdin.readline().rstrip()

# # 정수를 저장하는 큐 구현
# q = list()

# # 명령
# N = int(input())
# for _ in range(N):
#     cmd = input().split()
#     if cmd[0] == 'push':
#         q.append(int(cmd[1]))
#     elif cmd[0] == 'pop':
#         if any(q):
#             print(q.pop(0))
#         else:
#             print(-1)
#     elif cmd[0] == 'size':
#         print(len(q))
#     elif cmd[0] == 'empty':
#         if any(q):
#             print(0)
#         else:
#             print(1)
#     elif cmd[0] == 'front':
#         if any(q):
#             print(q[0])
#         else:
#             print(-1)
#     elif cmd[0] == 'back':
#         if any(q):
#             print(q[-1])
#         else:
#             print(-1)
#     else:
#         pass


import queue

n = int(input())
q = queue.Queue()
for _ in range(n):
    cmd, *num = input().split()
    if cmd == 'push':
        q.put(int(num[0]))
    elif cmd == 'pop':
        print(q.get() if not q.empty() else -1)
    elif cmd == 'size':
        print(q.qsize())
    elif cmd == 'empty':
        print(1 if q.empty() else 0)
    elif cmd == 'front':
        print(q.queue[0] if not q.empty() else -1)
    elif cmd == 'back':
        print(q.queue[-1] if not q.empty() else -1)
