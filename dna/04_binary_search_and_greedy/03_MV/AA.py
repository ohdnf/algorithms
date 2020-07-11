import sys
input = lambda: sys.stdin.readline()

def count(cap):
    size = 0
    cnt = 1
    for song in songs:
        if size + song > cap:
            cnt += 1
            size = song
        else:
            size += song
    return cnt

n, m = map(int, input().split())
songs = list(map(int, input().split()))

sm = 1
lg = sum(songs)
max_song = max(songs)
res = 0

while sm <= lg:
    mid = (sm + lg) // 2
        
    if mid >= max_song and count(mid) <= m:
        lg = mid - 1
        res = mid
    else:
        sm = mid + 1

print(res)