import sys
sys.stdin = open('input.txt')

def find_palindrome(string, length):
    result = 0
    for i in range(8-length+1):
        s = string[i:i+length]
        if s == s[::-1]:
            result += 1
    return result


for test_case in range(1, 11):
    length = int(input())
    horizon = []
    total = 0
    for _ in range(8):
        text = input().strip()
        horizon.append(text)
        total += find_palindrome(text, length)
    for vertical in list(zip(*horizon)):
        text = ''.join(vertical)
        total += find_palindrome(text, length)
    print('#{} {}'.format(test_case, total))
    