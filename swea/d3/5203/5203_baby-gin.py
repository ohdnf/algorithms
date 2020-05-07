import sys
sys.stdin = open('input.txt')

def baby_gin(hands):
    for idx in range(8):
        if hands[idx] >= 3 or hands[idx] and hands[idx+1] and hands[idx+2]:
            return True
    for idx in range(8, 10):
        if hands[idx] >= 3:
            return True

t = int(input())
for test_case in range(1, 1+t):
    cards = list(map(int, input().split()))
    player1 = [0]*10
    player2 = [0]*10
    result = 0
    for idx in range(12):
        number = cards[idx]
        # draw card
        if idx % 2:
            player2[number] += 1
        else:
            player1[number] += 1
        # baby-gin?
        if baby_gin(player1):
            result = 1
            break
        elif baby_gin(player2):
            result = 2
            break
    print('#{} {}'.format(test_case, result))
        