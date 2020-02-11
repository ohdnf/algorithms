import sys
input = lambda: sys.stdin.readline()

n = int(input())
progression = list(map(int, input().split()))

max_asc = max_dsc = tmp_asc = tmp_dsc = 1
for i in range(1, n):
    before = progression[i-1]
    after = progression[i]
    if before > after:
        tmp_dsc += 1
        if tmp_asc > max_asc:
            max_asc = tmp_asc
        tmp_asc = 1
    elif before < after:
        tmp_asc += 1
        if tmp_dsc > max_dsc:
            max_dsc = tmp_dsc
        tmp_dsc = 1
    else:
        tmp_asc += 1
        tmp_dsc += 1
if tmp_asc > max_asc:
    max_asc = tmp_asc
if tmp_dsc > max_dsc:
    max_dsc = tmp_dsc
result = max(max_asc, max_dsc)
print(result)