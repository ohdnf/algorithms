import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
users = []
for i in range(N):
    user = input().split()
    users.append([i, int(user[0]), user[1]])
users = sorted(users, key=lambda user: (user[1], user[0]))

for _, age, name in users:
    print(age, name)