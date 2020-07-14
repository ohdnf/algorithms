import sys
input = lambda: sys.stdin.readline()

l = int(input())
heights = list(map(int, input().split()))
m = int(input())

box = [0] * 100

max_h = 0
min_h = 100
for h in heights:
    box[h] += 1
    if h > max_h: max_h = h
    if h < min_h: min_h = h

for _ in range(m):
    # 높이가 제일 높은 상자 하나 빼기
    if box[max_h] == 1:
        box[max_h] -= 1
        max_h -= 1
        box[max_h] += 1
    else:
        box[max_h] -= 1
        box[max_h-1] += 1
    
    # 높이가 제일 낮은 상자 하나 넣기
    if box[min_h] == 1:
        box[min_h] -= 1
        min_h += 1
        box[min_h] += 1
    else:
        box[min_h] -= 1
        box[min_h+1] += 1

print(max_h - min_h)