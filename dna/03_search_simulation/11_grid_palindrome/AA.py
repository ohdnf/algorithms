import sys
input = lambda: sys.stdin.readline()

def isPalindrome(numbers):
    return True if numbers == numbers[::-1] else False

matrix = [list(map(int, input().split())) for _ in range(7)]
rev = list(zip(*matrix))

palindromes = 0

for i in range(7):
    for j in range(0, 3):
        if isPalindrome(matrix[i][j:j+5]):
            palindromes += 1
        if isPalindrome(rev[i][j:j+5]):
            palindromes += 1

print(palindromes)