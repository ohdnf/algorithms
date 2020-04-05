h, w = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(h)]

hour = last = 0
# for row in range(h):
#     for col in range(w):
#         if cheese[row][col]:
#             last += 1

def find(width, height, cheese):
    for row in range(height):
        for col in range(width):
            if cheese[row][col]:
                return True
    return False

def melt(width, height, cheese):
    return

while find(w, h, box):
    hour += 1
    last = melt(w, h, box)

print(hour, last)