def solution(word):
    order = {
        'A': 0,
        'E': 1,
        'I': 2,
        'O': 3,
        'U': 4
    }
    l = len(word)
    answer = 0
    weight = 781
    while l:
        answer += weight * order[word[-l]]
        weight = (weight - 1) // 5
        l -= 1
        answer += 1
    return answer
