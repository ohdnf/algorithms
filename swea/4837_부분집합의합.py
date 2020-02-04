A = list(range(1, 13))
subsets = []

for num in range(2**12):
    part = [A[idx] for idx, status in enumerate(list(format(num, '012b'))) if int(status)]
    subsets.append(part)

T = int(input())
for t in range(1, 1+T):
    n, k = map(int, input().split())
    cnt = 0
    for subset in subsets:
        if len(subset) == n and sum(subset) == k:
            cnt += 1

    print('#{0} {1}'.format(t, cnt))