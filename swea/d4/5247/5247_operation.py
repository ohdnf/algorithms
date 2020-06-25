import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs(start, goal):
    q = deque([start, ])
    visited = [0] * 1000001
    while q:
        num = q.popleft()
        for nxt in (num*2, num-1, num+1, num-10):
            if 0 < nxt <= 1000000 and not visited[nxt]:
                if nxt == goal:
                    return visited[num] + 1
                else:
                    visited[nxt] = visited[num] + 1
                    q.append(nxt)

t = int(input())
for test_case in range(1, t+1):
    N, M = map(int, input().split())
    trial = bfs(N, M)
    print('#{} {}'.format(test_case, trial))
