from collections import deque as dq

def solution(people, limit):
    answer = 0
    people.sort()
    people = dq(people)
    while len(people) > 1:
        if limit - people[-1] >= people[0]:
            people.pop()
            people.popleft()
        else:
            people.pop()
        answer += 1
    if people:
        answer += 1
    return answer

