import sys
input = lambda: sys.stdin.readline()

def reverse(num):
    return int(num[::-1])

def isPrime(num):
    max_aliquot = int(num ** 0.5)
    for aliquot in range(2, max_aliquot+1):
        if not num % aliquot:
            return False
    return True

n = int(input())
numbers = input().split()

res = list()

for number in numbers:
    rev_num = reverse(number)
    if rev_num <= 1:
        continue
    if isPrime(rev_num):
        res.append(rev_num)

print(*res, sep=' ')