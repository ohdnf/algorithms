import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self, arr):
        self.head = Node(arr[0])
        before = self.head
        for i in range(1, len(arr)):
            curr = Node(arr[i])
            before.nxt = curr
            before = curr

    def insert(self, idx):
        curr = self.head
        curr_idx = 0

        while curr_idx < idx:
            curr = curr.nxt
            curr_idx += 1
        
        insert_val = 0
        if curr.nxt:
            insert_val = curr.val + curr.nxt.val
        else:
            insert_val = curr.val + self.head.val
        new = Node(insert_val)
        new.nxt = curr.nxt
        curr.nxt = new
    
    def __repr__(self):
        curr = self.head
        result = str(curr.val)
        while curr.nxt:
            curr = curr.nxt
            result += ' ' + str(curr.val)
        return result


t = int(input())
for test_case in range(1, t+1):
    n, m, k = map(int, input().split())
    numbers = LinkedList(list(map(int, input().split())))
    idx = 0
    for _ in range(k):
        idx = (idx + m) % (n - 1)
        numbers.insert(idx)
        n += 1

    print('#{} {}'.format(test_case, numbers))