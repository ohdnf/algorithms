import sys
input = lambda: sys.stdin.readline().rstrip()

# 등수 산정 기준
# 1. 문제를 많이 푼 순
# 2. 푼 문제 수가 같을 경우 '총 시간'이 작은 순
# 총 시간 = (각 문제의 경과 시간의 합) + (통과 이전 해당 문제에 틀린 답을 제출한 횟수) * 20

# 채점 결과
# AC: 통과
# RE, TLE, WA: 오답

# 참가 팀 수, 문제 수, 채점로그의 개수
n, m, q = map(int, input().split())

# 팀: 푼 문제 수, 총 시간
teams = [[[0]*m, [0]*m] for _ in range(n)]

# 채점정보: 경과 시간, 팀 번호, 문제 번호, 채점 결과
for i in range(q):
    elapsed, team_num, que_num, result = input().split()
    if result == 'AC':
        pass
