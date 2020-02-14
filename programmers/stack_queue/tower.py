# def solution(heights):
#     answer = [0 for _ in range(len(heights))]
#     while len(heights) > 1:
#         height = heights.pop()
#         i = len(heights)
#         for j in range(len(heights)-1, -1, -1):
#             if heights[j] > height:
#                 answer[i] = j+1
#                 break
#     return answer

# 강사님 풀이
# 순방향 순회
# def solution(heights):
#     answer = []
#     for i in range(len(heights)):
#         for j in range(i, -1, -1):
#             if heights[i] < heights[j]:
#                 answer.append(j+1)
#                 break
#         else:
#             answer.append(0)
#     return answer

# 스택 활용
def solution(heights):
    answer = []
    for i in range(len(heights)):
        stack = []
        for j in range(i):
            if heights[i] < heights[j]:
                stack.append(j+1)
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(0)
    return answer


if __name__ == "__main__":
    print(solution([6,9,5,7,4]))
    print(solution([3,9,9,3,5,7,2]))
    print(solution([1,5,3,6,7,6,5]))