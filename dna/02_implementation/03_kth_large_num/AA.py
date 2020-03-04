import sys
sys.stdin = open('in1.txt')

def get_three(idx, total, limit, hap):
    if idx == len(cards):
        if total == limit:
            three.add(hap)
    elif total == limit:
        three.add(hap)
    else:
        used[idx] = True
        get_three(idx+1, total+1, limit, hap+cards[idx])
        used[idx] = False
        get_three(idx+1, total, limit, hap)

n, k = map(int, input().split())
cards = list(map(int, input().split()))
used = [False for _ in range(n)]
three = set()
get_three(0, 0, 3, 0)
three = sorted(list(three), reverse=True)
print(three[k-1])