def traversal(v, n):
    if v > n:
        return
    else:
        # print(v, end=' ')     # 전위 순회
        traversal(v*2)
        # print(v, end=' ')     # 중위 순회
        traversal(v*2+1)
        print(v, end=' ')       # 후위 순회


if __name__ == '__main__':
    traversal(1, 7)     # 1부터 7까지 완전이진트리 순회