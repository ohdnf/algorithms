import sys
input = lambda: sys.stdin.readline().rstrip()

width, height = map(int, input().split())
cuts = int(input())
v_cut = [0, width]
h_cut = [0, height]
for _ in range(cuts):
    orientation, index = map(int, input().split())
    if orientation: # Vertical
        v_cut.append(index)
    else:   # Horizontal
        h_cut.append(index)

max_w = max_h = 0
h_cut.sort()
v_cut.sort()
for i in range(1, len(v_cut)):
    w = v_cut[i] - v_cut[i-1]
    if w > max_w:
        max_w = w
for i in range(1, len(h_cut)):
    h = h_cut[i] - h_cut[i-1]
    if h > max_h:
        max_h = h
print(max_w * max_h)