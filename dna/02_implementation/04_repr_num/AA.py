import sys
input = lambda: sys.stdin.readline()
# sys.stdin = open('in1.txt')
n = int(input())
scores = list(map(int, input().split()))
avg = sum(scores)//n
students = [[abs(avg-score), score, idx+1] for idx, score in enumerate(scores)]
students.sort(key=lambda s: s[0])
result = list()
min_value = students[0][0]
for d, s, i in students:
    if d == min_value:
        result.append((s, i))
    else:
        break
if len(result) <= 2:
    result.sort(key=lambda s: -s[0])
else:
    result.sort(key=lambda s: s[1])
score, number = result[0]
print(score, number)