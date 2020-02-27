import sys
sys.stdin = open('input.txt')
import time
start = time.time()

class Node:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt

class LinkedList:
    def __init__(self, arr):
        self.head = Node(arr[0])
        curr = self.head
        for i in range(1, len(arr)):
            new = Node(arr[i], curr)
            curr.nxt = new
            curr = new
        self.tail = curr

    def search(self, idx):
        curr = self.head
        curr_idx = 0
        while curr_idx < idx:
            curr = curr.nxt
            curr_idx += 1
        return curr
    
    def find_bigger_than(self, val):
        curr = self.head
        curr_idx = 0
        while curr.nxt:
            if curr.val > val:
                return curr_idx
            else:
                curr = curr.nxt
                curr_idx += 1
        return curr_idx
        
    def __repr__(self):
        result = ''
        curr = self.head
        while curr.nxt:
            result += str(curr.val) + ' '
            curr = curr.nxt
        result += str(curr.val)
        return result

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    seq = LinkedList(list(map(int, input().split())))
    for _ in range(m-1):
        incoming = LinkedList(list(map(int, input().split())))
        first = incoming.head.val
    # 추후 수정
    
    print('#{} {}'.format(test_case, seq))

print(time.time() - start, 's')