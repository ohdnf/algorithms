import sys
sys.stdin = open('input.txt')


def tournament(players):
    if len(players) == 1:
        return players[0]
    elif len(players) == 2:
        return rsp(players[0], players[1])
    else:
        i = 0
        j = len(players)-1
        return rsp(tournament(players[:(i+j)//2+1]), tournament(players[(i+j)//2+1:]))

def rsp(first, second):
    first_card = first[1]
    second_card = second[1]
    if first_card == second_card:
        return second if first[0] > second[0] else first
    elif first_card==1 and second_card==2:
        return second
    elif first_card==1 and second_card==3:
        return first
    elif first_card==2 and second_card==1:
        return first
    elif first_card==2 and second_card==3:
        return second
    elif first_card==3 and second_card==1:
        return second
    elif first_card==3 and second_card==2:
        return first


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    players = [[player, card] for player, card in enumerate(list(map(int, input().split())))]
    # stack = []
    winner = tournament(players)
    print('#{} {}'.format(test_case, winner[0]+1))