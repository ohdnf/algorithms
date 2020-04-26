import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    # total, leafs, target
    n, m, l = map(int, input().split())
    tree = [0]*n
    leafs = list()
    for _ in range(m):
        idx, num = map(int, input().split())
        tree[idx-1] = num

    if n % 2 == 0:
        tree[(n-1) // 2] = tree[n-1]
        n -= 1
    for idx in range(n-1, 0, -2):
        tree[(idx-1) // 2] = tree[idx-1] + tree[idx]
    #     print(f'tree[{(idx-1) // 2}] = tree[{idx-1}] + tree[{idx}]  ==> {tree[(idx-1) // 2]} = {tree[idx-1]} + {tree[idx]}')
    # print(tree)
    print('#{} {}'.format(test_case, tree[l-1]))