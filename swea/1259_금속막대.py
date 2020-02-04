import sys
sys.stdin = open('input.txt')

def connect(screws):
    
    return 0

T = int(input())
for t in range(1, T+1):
    n = int(input())
    d = list(map(int, input().split()))
    screws = []
    for i in range(0, n*2, 2):
        screws.append((d[i], d[i+1]))
    
    print(screws)