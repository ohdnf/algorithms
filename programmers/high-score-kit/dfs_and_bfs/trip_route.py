def solution(tickets):
    answer = []

    total = len(tickets) + 1        # 방문할 모든 공항 수
    used = [False] * len(tickets)   # 항공권 사용 여부

    def dfs(route):
        if len(route) == total:     # 모든 항공권을 사용한 경로
            answer.append(route)
        else:
            for idx, ticket in enumerate(tickets):
                # 아직 안 쓴 항공권 & 출발지가 경로의 마지막 공항
                if not used[idx] and route[-1] == ticket[0]:
                    used[idx] = True
                    dfs(route+[ticket[1]])
                    used[idx] = False
    
    for idx, ticket in enumerate(tickets):
        if ticket[0] == 'ICN':  # 항상 "ICN" 공항에서 출발
            used[idx] = True
            dfs(ticket)
            used[idx] = False
    
    answer.sort()   # 경로가 2개 이상일 경우 알파벳 오름차순으로 정렬

    return answer[0]


# 다른 사람의 풀이
from collections import defaultdict 

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1: # 경로 완성
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)     # 항공권 사용

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)   # 도착지를 다시 출발지로 설정해 DFS 탐색

        graph[key].insert(idx, country) # 항공권 초기화

        if ret:     # 경로 완성되었을 경우 반환 호출
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)   # 초깃값이 빈 배열인 경로

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])  # 출발지에서 갈 수 있는 도착지 등록
        graph[ticket[0]].sort()             # 알파벳 순으로 정렬

    answer = dfs(graph, N, "ICN", ["ICN"])  # ICN 공항에서 출발

    return answer


if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]), ["ICN", "JFK", "HND", "IAD"])
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]), ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
