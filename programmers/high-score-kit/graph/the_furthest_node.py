from collections import deque as dq

def solution(n, edge):
    answer = 0
    graph = {node: [] for node in range(1,n+1)}
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n+1)
    max_distance = 0
    queue = dq()
    queue.append((1,0))
    visited[1] = True
    while queue:
        curr, dist = queue.popleft()
        if dist > max_distance:
            max_distance = dist
            answer = 1
            # print('max dist changed')
        elif dist == max_distance:
            answer += 1
        for nxt in graph[curr]:
            if not visited[nxt]:
                queue.append((nxt, dist+1))
                visited[nxt] = True
        # print(curr, dist, answer)
    return answer


if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)


"""
오답노트

- BFS로 풀이했다.
- 방문 체크를 queue에서 꺼낼 때 했는데 1번 노드를 넣을 때 방문 체크를 안 해줘서 조금 헤맸다.
- 방문 체크의 위치를 중복 방문 없도록 설정해야한다.
"""