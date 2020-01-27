T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sieve = [True] * N
    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, N, i):
                sieve[j] = False
    primes = [number for number in range(2, N) if sieve[number]]
    len_primes = len(primes)
    result = 0
    for x in range(len_primes):
        for y in range(x, len_primes):
            for z in range(y, len_primes):
                if primes[x] + primes[y] + primes[z] == N:
                    result += 1
    print('#{0} {1}'.format(test_case, result))