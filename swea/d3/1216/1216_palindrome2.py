import sys
sys.stdin = open('input.txt')

def find_max_palindrome(string):
    for length in range(100, 1, -1):
        for i in range(100-length+1):
            s = string[i:i+length]
            if s == s[::-1]:
                return len(s)


for _ in range(10):
    test_case = int(input())
    result = 1
    horizon = []
    for _ in range(100):
        text = input().strip()
        horizon.append(text)
        palindrome = find_max_palindrome(text)
        if palindrome > result:
            result = palindrome
    for vertical in list(zip(*horizon)):
        text = ''.join(vertical)
        palindrome = find_max_palindrome(text)
        if palindrome > result:
            result = palindrome
    print('#{} {}'.format(test_case, result))