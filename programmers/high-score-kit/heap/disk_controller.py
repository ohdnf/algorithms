from collections import deque as dq
from math import floor
import heapq as hq

def solution(jobs):
    tasks = dq(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    waiting = []
    hq.heappush(waiting, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(waiting) > 0:
        dur, arr = hq.heappop(waiting)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            hq.heappush(waiting, tasks.popleft())
        if len(tasks) > 0 and len(waiting) == 0:
            hq.heappush(waiting, tasks.popleft())
    return total_response_time // len(jobs)


def my_solution(jobs):
    """
    작업 요청 시점, 작업 소요 시간
    작업 요청부터 종료까지 걸린 시간 = (작업 소요 시간) + (작업 시작 시간) - (작업 요청 시간)
    """
    answer = 0  # 각 작업의 요청-종료 시간의 총합
    time = 0    # 시간 단위: ms
    length = len(jobs)  # 작업 수
    jobs = sorted(jobs, key=lambda j: (-j[0], -j[1]))   # 작업 정렬
    waiting = []    # 대기 작업 배열
    curr = []

    while curr or waiting or jobs:
        while jobs and jobs[-1][0] <= time:
            waiting.append(jobs.pop())
        if curr:
            if curr[0] <= time:
                answer += curr[0] - curr[1]
                curr = []
        if not curr and waiting:
            waiting.sort(key=lambda job: -job[1])
            request, estimated = waiting.pop()
            curr = [time+estimated, request]

        # print(f'time: {time} / curr: {curr} / waiting: {waiting} / jobs: {jobs} / answer: {answer}')
        time += 1
    return floor(answer / length)


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))
