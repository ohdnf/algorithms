# DFS

answer = 0

def solution(numbers, target):    
    def dfs(level, number):
        global answer
        if level == len(numbers):
            if number == target:
                answer += 1
        else:
            dfs(level+1, number+numbers[level])
            dfs(level+1, number-numbers[level])
    dfs(0, 0)
    return answer

# 다른 사람의 풀이 1

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 다른 사람의 풀이 2

from itertools import product

def solution1(numbers, target):
    l = [(x, -x) for x in numbers]
    # print(list(product(*l)))
    s = list(map(sum, product(*l)))
    return s.count(target)


# solution1([1, 1, 1, 1, 1], 3)
solution1([1, 2, 3, 4, 5], 3)
