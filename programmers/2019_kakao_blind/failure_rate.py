# 예전 풀이
def old_solution(N, stages):
    answer = []
    fail = []
    for stage in range(1, N + 1):
        total = 0
        ing = 0
        for user in stages:
            if user > stage:
                total += 1
            elif user == stage:
                total += 1
                ing += 1
                
        if ing != 0 and total != 0:
            fail.append({"stage": stage, "rate": (ing / total)})
        else:
            fail.append({"stage": stage, "rate": 0})
    
    fail = sorted(fail, key=lambda k: k["rate"], reverse=True)
    answer = [item["stage"] for item in fail]
    
    return answer

# 2020-09-10 풀이
def solution(N, stages):
    # N: 전체 스테이지의 개수
    # stages: 사용자가 현재 도전하는 스테이지 번호의 배열
    # answer: 실패율이 높은 스테이지부터 내림차순으로 정렬한 스테이지 번호의 배열
    answer = []

    # 현재 도전 중인 스테이지 번호 역순으로 사용자 정렬
    stages = sorted(stages, reverse=True)
    
    # 현재 스테이지 도달한 사용자 수
    passed = len(stages)
    
    # 스테이지 순으로 실패율 계산
    for stage in range(1, N+1):
        # 현재 스테이지에 있는 사용자 수 찾기
        count = 0
        while stages and stages[-1] == stage:
            stages.pop()
            count += 1
        # 실패율 = 현재 스테이지에 있는 사용자의 수 / 스테이지 도달한 사용자 수
        rate = count / passed if count != 0 else 0
        answer.append([rate, stage])    # [실패율, 스테이지 번호]
        passed -= count
    
    # 실패율(내림차순) > 스테이지 번호(오름차순) 정렬
    answer = [stage for _, stage in sorted(answer, key=lambda s: (-s[0], s[1]))]
    return answer


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4,4,4,4,4]))