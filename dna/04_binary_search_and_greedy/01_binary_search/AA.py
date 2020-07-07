import sys
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

def binary_search(num, l, r):
    c = (l + r) // 2
    if numbers[c] == num:
        return c
    elif numbers[c] > num:
        return binary_search(num, l, c)
    elif numbers[c] < num:
        return binary_search(num, c, r)

res = binary_search(m, 0, n-1)
print(res + 1)