ALPHABET = 'ABCDEFGHIJKLMN OPQRSTUVWXYZ'

def solution(name):
    answer = 0
    name = [ord(alphabet)-65 for alphabet in name]
    length = len(name)
    head = 0
    print(head, name)
    while any(name):
        answer += min(name[head], 26-name[head])
        name[head] = 0
        print(head, name, answer)

        if not any(name):
            break

        left = head
        left_move = 0
        while name[left] == 0:
            left -= 1
            left_move += 1
            if left < 0:
                left += length
        
        right = head
        right_move = 0
        while name[right] == 0:
            right += 1
            right_move += 1
            if right >= length:
                right -= length
        
        if left_move >= right_move:
            head = right
            answer += right_move
        else:
            head = left
            answer += left_move

    return answer


if __name__ == "__main__":
    print(solution("JAZ"), 11)
    print(solution("JEROEN"), 56)
    print(solution("JAN"), 23)
    print(solution("BBBAAAB"), 9)
    print(solution("ABABAAAAABA"), 11)