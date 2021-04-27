T = int(input())
prime = [True] * 1000000
for i in range(2, int(1000000 ** 0.5) + 1):
    for j in range(i * 2, 1000000, i):
        prime[j] = False

for _ in range(T):
    N = int(input())
    goldbach = 0
    for first in range(2, N // 2 + 1):
        if prime[first] and prime[N - first]:
            goldbach += 1
    print(goldbach)
