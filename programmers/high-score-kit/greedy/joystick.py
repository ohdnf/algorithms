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
    print(solution("ABAAABAAAAAAB"), 12)
    print(solution("BABAAAAAAAAAB"), 8)


"""
로직
1. 각 자리의 알파벳 ord값에서 ord("A")값을 감산
2. 현재 커서 위치의 알파벳 조작
3. 왼쪽과 오른쪽 중 최소 이동으로 커서 위치 변경
(이 때, 조건에서 커서가 맨 오른쪽에서 이동할 경우 첫 번째 문자로 갈 수 있다고 명시되지 않았으므로
왼쪽과 오른쪽이 같을 경우엔 왼쪽으로 오른쪽으로 )
"""