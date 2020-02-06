import sys
# sys.stdin = open('input.txt')
sys.stdin = open('C:/Users/multicampus/Workspace/algorithms/swea/d5/1259/input.txt')

# binary_tree 방식으로 짜보자 tree 만들고 insert 하는 형식으로!

# def connect(stick, screws):
#     while screws:   # 나사가 안 남을 때까지
#         screw = screws.pop()
#         if screw[0] == stick[-1]:
#             stick = stick + ' ' + screw
#         elif screw[-1] == stick[0]:
#             stick = screw + ' ' + stick
#         else:
#             screws.append(screw)
    
# def connect(stick, screws):
#     if all(used): # 안 쓴 나사가 없으면
#         return stick
#     else:
#         for i in range(n): # 남은 나사 중 하나 가져오기
#             if used[i]:
#                 pass
#             else:
#                 screw = screws[i]
#                 used[i] = True
#                 if screw[0] == stick[-1]: # 수나사가 스틱의 암나사과 맞을 때
#                     stick + ' ' + screw
#                     return connect(new_stick, screws)
#                 elif screw[-1] == stick[0]: # 암나사가 스틱의 수나사와 맞을 때
#                     new_stick = screw + ' ' + stick
#                     return connect(new_stick, screws)
#                 # else: # 맞지 않을 때
#                 #     used[i] = False
#                 #     connect(stick, screws)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    d = list(map(int, input().split()))
    
    screws = []
    for i in range(0, n*2, 2):
        screws.append(str(d[i]) + ' ' + str(d[i+1]))

    used = [False for _ in range(n)]
    sticks = []
    for i in range(n):
        stick = screws[i]
        used[i] = True
        # new_stick = connect(stick, screws)
        # print('new stick:', new_stick)
        # sticks.append(new_stick)

    # print(sticks)
    