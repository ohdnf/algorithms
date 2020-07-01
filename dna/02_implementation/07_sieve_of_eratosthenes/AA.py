import sys
input = lambda: sys.stdin.readline()

num = int(input())

sieve = [True] * (num+1)
sieve[0], sieve[1] = False, False
for i in range(2, int(num ** 0.5)+1):
    if sieve[i]:
        for j in range(i*2, num+1, i):
            sieve[j] = False
primes = [i for i in range(2, num+1) if sieve[i]]
print(len(primes))