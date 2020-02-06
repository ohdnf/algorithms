T = int(input())
for t in range(1, T+1):
    S = input()
    cards = {'S': [], 'D': [], 'H': [], 'C': []}
    result = ''
    # 가진 카드 파악
    for i in range(0, len(S), 3):
        card = [S[i], S[i+1:i+3]]
        # 중복 카드 검사
        if card[1] in cards[card[0]]:
            result = 'ERROR'
            break
        else:
            cards[card[0]].append(card[1])
    
    if result != 'ERROR':
        for pattern in ['S', 'D', 'H', 'C']:
            result += str(13 - len(cards[pattern])) + ' '
        result = result.strip()
    
    print('#{} {}'.format(t, result))
