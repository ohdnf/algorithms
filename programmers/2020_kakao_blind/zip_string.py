def solution(s):
    answer = len(s)
    for size in range(1, len(s)//2+1):
        chunk = [[s[:size], 1]]
        for i in range(size, len(s) - (len(s) % size), size):
            if s[i:i+size] == chunk[-1][0]:
                chunk[-1][1] += 1
            else:
                chunk.append([s[i:i+size], 1])
        chunk.append([s[len(s) - (len(s) % size):], 1])
        string = ''
        for ch in chunk:
            if ch[1] > 1:
                string += str(ch[1]) + ch[0]
            else:
                string += ch[0]
        # print(string)
        answer = min(answer, len(string))
    return answer

if __name__ == "__main__":
    strings = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    for string in strings:
        print(solution(string))
    # print(solution("aabbaccc"))
    # result: 7 9 8 14 17
