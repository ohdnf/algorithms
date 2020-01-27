T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sieve = [True] * N
    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, N, i):
                sieve[j] = False
    prime_numbers = [number for number in range(2, N) if sieve[number]]
    print(prime_numbers)