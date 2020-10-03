from collections import deque as dq

def solution(n, computers):
    answer = 0
    checked = [False] * n
    
    for node in range(n):
        if not checked[node]:
            answer += 1
            q = dq()
            q.append(node)
            # find network
            while q:
                curr = q.popleft()
                checked[curr] = True
                for computer, connected in enumerate(computers[curr]):
                    if connected and not checked[computer]:
                        q.append(computer)

    return answer


if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
