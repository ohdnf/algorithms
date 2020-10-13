from collections import deque as dq
from collections import defaultdict


# 나의 풀이
def solution(n, results):
    answer = 0
    # 해당 선수가 이긴 선수와 진 선수를 구분해 저장
    records = {player: {'w': [], 'l': []} for player in range(1, n + 1)}
    for a, b in results:
        records[a]['w'].append(b)
        records[b]['l'].append(a)
    # 각 선수별로 그래프 순회하며 순위 판단
    for player in range(1, n + 1):
        # 내가 진 선수가 또 진 선수 재귀
        q = dq(records[player]['l'])
        while q:
            winner = q.popleft()
            for other in records[winner]['l']:
                if other in records[player]['l']:
                    continue
                else:
                    records[player]['l'].append(other)
                    q.append(other)
        # 내가 이긴 선수가 또 이긴 선수 재귀
        q = dq(records[player]['w'])
        while q:
            loser = q.popleft()
            for other in records[loser]['w']:
                if other in records[player]['w']:
                    continue
                else:
                    records[player]['w'].append(other)
                    q.append(other)
        # 해당 선수의 순위가 확정되려면 n-1명에 대한 판단이 있어야 함
        if len(records[player]['w']) + len(records[player]['l']) == n - 1:
            answer += 1
    return answer


# 다른 사람의 풀이
def solution2(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])

    for i in range(1, n+1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])

        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)


"""
오답노트

소요 시간: 약 1시간 반

우선 한 번 이기면 계속 이긴다는 조건이 있으므로,
어떤 선수의 정확한 순위는 나머지 모든 선수와의 관계가 파악될 때 알 수 있다.
처음에는 그래프 탐색을 통해서 구하나 싶었는데, 순위는 경로 탐색으로 정해지지 않으므로
좋은 문제 풀이 방법이 아니다(이를 깨닫는데 많은 시간이 소요됐다)

주어진 승패 결과를 토대로 어떤 한 선수가 이긴 선수와 진 선수를 분류할 수 있다.
분류된 결과를 바탕으로 다시 전체 선수를 돌면서
어떤 한 (현재)선수가
졌던 선수의 진 선수 목록을,
이겼던 선수의 이긴 선수 목록을,
재귀적으로 탐색하며 현재 선수의 진 선수 목록과 이긴 선수 목록에 추가해준다.
이렇게 하면 결과적으로 한 선수의 이긴 선수 목록과 진 선수 목록의 길이 합이 n-1일 때
정확한 순위를 알 수 있게 된다.  

파이썬 데이터 구조를 사용해서 시간 복잡도를 줄이려고 했으나
오히려 단순배열로 처리를 하니 구현이 빨랐다.
다음부터는 우선 배열로 처리하고 데이터 구조를 바꾸는 전략을 택해야겠다.

다른 사람의 풀이를 보면 내가 각 선수별 순위를 업데이트하는 부분을
set로 처리하였다. 코드 줄 수가 매우 간결해졌다.

인터넷을 찾아보니 플로이드-와샬 알고리즘으로 풀 수 있다고 한다.
"""