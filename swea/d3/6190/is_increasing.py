n = 1357

# mono-increasing?
def check(n):
    n, r = n // 10, n % 10
    while n > 9:
        if n%10 > r:
            return False
        n, r = n // 10, n % 10
    return True

if __name__ == "__main__":
    print(check(n))
