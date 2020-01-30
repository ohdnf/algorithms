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

# 팀: 총 시간, 푼 문제
team_time = [ [0]*m for _ in range(n) ]
team_problem = [ [False]*m for _ in range(n) ]

# 채점로그: 경과 시간, 팀 번호, 문제 번호, 채점 결과
for i in range(q):
    elapsed, team, problem, result = input().split()
    elapsed = int(elapsed)
    team = int(team) - 1
    problem = int(problem) - 1
    # 이미 푼 문제일 경우
    if team_problem[team][problem]:
        pass
    # 풀지 못한 문제일 경우
    else:
        # 통과
        if result == 'AC':
            team_time[team][problem] += elapsed
            team_problem[team][problem] = True
        # 실패
        else:
            team_time[team][problem] += 20

# 팀마다 등수 기준 산정
teams = []
for i in range(n):
    total_accepted = sum(team_problem[i])
    total_time = sum([t for p, t in zip(team_problem[i], team_time[i]) if p])
    teams.append([i+1, total_accepted, total_time])

teams = sorted(teams, key=lambda t: (-t[1], t[2], t[0]))

for team in teams:
    print(team[0], team[1], team[2])