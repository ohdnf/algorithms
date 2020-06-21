import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    N, M = map(int, input().split())
    friendships = { num: list() for num in range(1, N+1) }
    for _ in range(M):
        a, b = map(int, input().split())
        friendships[a].append(b)    # a < b
        friendships[b].append(a)
    
    # total = 0
    best_friends = friendships[1]
    total = set(best_friends)
    for bf in best_friends:
        total |= set(friendships[bf])
    total -= {1,}
    print('#{} {}'.format(test_case, len(total)))