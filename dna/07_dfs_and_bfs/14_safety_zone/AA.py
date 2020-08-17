from collections import deque as dq
import sys
# sys.stdin = open("in1.txt")

d = ((0,1),(1,0),(0,-1),(-1,0))

n = int(input())
area = list()
precipitations = set()
for _ in range(n):
    line = list(map(int, input().split()))
    area.append(line)
    for h in line:
        precipitations.add(h)

max_safe_area = 0

# 모든 강수량에 대해 안전 지역 개수 검사
for p in precipitations:
    # 침수 지역 초기화
    flooded = [[False]*n for _ in range(n)]
    # 침수 지역 표시
    for row in range(n):
        for col in range(n):
            if area[row][col] <= p:
                flooded[row][col] = True
    safe_area = 0
    # 안전 지역 검사
    for row in range(n):
        for col in range(n):
            if not flooded[row][col]:
                search = dq()
                search.append((row, col))
                flooded[row][col] = True    # 안전지역 확인된 곳은 True로 변경
                while search:
                    crow, ccol = search.popleft()
                    for drow, dcol in d:
                        nrow, ncol = crow+drow, ccol+dcol
                        if 0<=nrow<n and 0<=ncol<n and not flooded[nrow][ncol]:
                            flooded[nrow][ncol] = True
                            search.append((nrow, ncol))
                safe_area += 1
    
    if max_safe_area < safe_area:
        max_safe_area = safe_area

print(max_safe_area)