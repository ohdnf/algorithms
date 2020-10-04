answer = float('inf')

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)

    def changable(from_word, to_word):
        same = 0
        for i in range(len(from_word)):
            if from_word[i] == to_word[i]:
                same += 1
        if len(from_word) - same == 1:
            return True
        return False

    def dfs(i, curr, step):
        global answer
        if curr == target:
            if answer > step:
                answer = step
        if i == len(words):
            if curr == target and answer > step:
                answer = step
        elif answer < step:
            return
        else:
            for j in range(len(words)):
                if not visited[j] and changable(curr, words[j]):
                    visited[j] = True
                    dfs(i+1, words[j], step+1)
                    visited[j] = False
    
    dfs(0, begin, 0)

    if answer == float('inf'):
        return 0
    return answer



# 다른 사람의 풀이
from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)


if __name__ == "__main__":
    print(solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 4)
    print(solution("hit", "cog", ["hot","dot","dog","lot","log"]), 0)


"""
오답노트

DFS로 풀었다. 문제 접근할 때 words의 인덱스를 모두 돌면서 비교하자고 생각한 부분이 맞았던 것 같다.
다른 사람들의 풀이는 BFS였는데 접근은 비슷했다. 다만 dictionary에 begin 단어로부터 거리를 계산한다는 개념이 새로웠다.
"""