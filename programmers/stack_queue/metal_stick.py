# 여러 개의 쇠막대기 레이저 절단
# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓임
# 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치면 안 됨
# 각 쇠막대기를 자르는 레이저는 적어도 하나 존재
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음

# () ==> 레이저
# ()(((()())(())()))(()) => 17

def solution(arrangement):
    answer = 0
    stack = ['(']
    sticks = 0
    arrangement = arrangement[1:]
    for ps in arrangement:
        if stack:
            if ps == ')':
                if stack[-1] == '(':
                    answer += sticks
                else:
                    sticks -= 1
                    answer += 1
            else:
                if stack[-1] == '(':
                    sticks += 1
        stack.append(ps)
    return answer

# def solution(arrangement):
#     answer = 0
#     stack = []
#     sticks = 0
#     before = '('
#     arrangement = arrangement[1:]
#     for ps in arrangement:
#         if stack:
#             if ps == ')':
#                 if before == '(':
#                     answer += sticks
#                 else:
#                     sticks -= 1
#                     answer += 1
#             else:
#                 if before == '(':
#                     sticks += 1
#         else:
#             stack.append(ps)
#         before = ps
#     return answer