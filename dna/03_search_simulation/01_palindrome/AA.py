import sys
input = lambda: sys.stdin.readline()

def is_palindrome(word):
    return 'YES' if word == word[::-1] else 'NO'

n = int(input())
for i in range(1, n+1):
    # word = input().lower()
    word = input().strip().lower()
    # print(word)
    res = is_palindrome(word)
    print(f'#{i} {res}')