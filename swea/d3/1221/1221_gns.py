import sys
sys.stdin = open('input.txt')

gns = (("ZRO", '0'), ("ONE", '1'), ("TWO", '2'), ("THR", '3'), ("FOR", '4'), ("FIV", '5'), ("SIX", '6'), ("SVN", '7'), ("EGT", '8'), ("NIN", '9'))

T = int(input())
for t in range(1, T+1):
    test_case, length = input().split()
    print(test_case)
    numbers = input()
    for g in gns:
        numbers = numbers.replace(g[0], g[1])
    numbers = sorted(map(int, numbers.split()))
    numbers = ' '.join(map(str, numbers))
    for g in gns:
        numbers = numbers.replace(g[1], g[0])
    print(numbers)