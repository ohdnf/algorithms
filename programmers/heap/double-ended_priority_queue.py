import heapq as hq

def solution(operations):
    answer = []

    for oper in operations:
        cmd, num = oper.split()
        if cmd == 'I':
            hq.heappush(answer, int(num))
        elif cmd == 'D' and answer:
            if num == '1':
                answer.pop()
            elif num == '-1':
                answer.pop(0)
        # print(answer)
    
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]


if __name__ == "__main__":
    res1 = solution(["I 16","D 1"])
    print(res1)
    res2 = solution(["I 7","I 5","I -5","D -1"])
    print(res2)
    res3 = solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
    print(res3)


"""
오답 노트
1. 단순히 deque랑 heapq를 혼합 ==> heapq는 list만 적용가능
2. answer[0], answer[-1]로 접근 ==> heap[0] heapq는 정렬된 리스트가 아니므로 이런 접근 X
"""

# 다른 풀이1
import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]


# 다른 풀이2
from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]
