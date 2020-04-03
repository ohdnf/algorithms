import sys
from collections import deque
sys.stdin= open('5102.txt')
T= int(input())
for tc in range(1,T+1):
    V,E=map(int,input().split())
    adj=[[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        v,w = map(int,input().split())
        adj[v][w]=1
        adj[w][v]=1
    S,G=map(int,input().split())
    que=deque()
    que.append((S,0))
    visited=[0]*(V+1)
    visited[S]=1
    while que:
        s, dist = que.popleft()
        if s==G:
            print('#{} {}'.format(tc, dist))
            break
        for i in range(V+1):
            if adj[s][i]==1 and visited[i]==0:
                visited[i]=1
                que.append((i,dist+1))
    else:
        print('#{} {}'.format(tc, 0))