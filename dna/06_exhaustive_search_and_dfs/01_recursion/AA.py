import sys
input = lambda: sys.stdin.readline()

n = int(input())

def binary(num, res):
    if num < 1:
        return res
    else:
        return binary(num//2, str(num%2)+res)

print(binary(n, ''))