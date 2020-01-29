import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
students = []
for _ in range(N):
    name, kor, eng, mat = input().split()
    students.append([name, int(kor), int(eng), int(mat)])

result = sorted(students, key=lambda s: (-s[1], s[2], -s[3], s[0]))

print(result)

for student in result:
    print(student[0])
