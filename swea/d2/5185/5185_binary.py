import sys
sys.stdin = open('input.txt')



t = int(input())
for test_case in range(1, t+1):
    n, hexdecimal = input().split()
    binary = ''
    for num in hexdecimal:
        if num.isdigit():
            binary += '{0:04b}'.format(int(num))
        else:
            binary += '{0:04b}'.format(int(num, 16))
    print('#{} {}'.format(test_case, binary))