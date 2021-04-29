import sys

N = int(input())
animals = list(map(int, input().split()))

cnt = [0] * N
for animal in animals:
    if animal >= N:
        print(0)
        sys.exit()
    cnt[animal] += 1

if cnt[0] == 0:
    print(0)
    sys.exit()

for c in cnt:
    if c > 2:
        print(0)
        sys.exit()

for idx in range(1, N):
    if cnt[idx] > cnt[idx - 1]:
        print(0)
        sys.exit()

combi = 1
for c in cnt:
    if c == 2:
        combi *= 2
if 1 in cnt:
    combi *= 2
print(combi)
