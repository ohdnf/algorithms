import sys
sys.stdin = open('input.txt')
import time
start = time.time()

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.length = 1
    
    def get(self, idx):
        curr = self.head
        curr_idx = 0

        while curr_idx < idx:
            curr = curr.nxt
            curr_idx += 1
        
        return curr.val
    
    def index(self, val):
        curr = self.head
        curr_idx = 0

        while curr:
            if curr.val == val:
                return curr_idx
            else:
                if curr.nxt:
                    curr = curr.nxt
                    curr_idx += 1
                else:
                    raise IndexError

    def insert(self, idx, val):
        curr = self.head
        curr_idx = 0

        while curr_idx < idx:
            curr = curr.nxt
            curr_idx += 1
        
        new = Node(val)
        new.nxt = curr.nxt
        curr.nxt = new

        self.length += 1
    
    def append(self, val):
        curr = self.head
        curr_idx = 0
        
        while curr.nxt:
            curr = curr.nxt
            curr_idx += 1
        
        new = Node(val)
        curr.nxt = new
        self.length += 1
    
    def appendleft(self, val):
        new = Node(val)
        new.nxt = self.head
        self.head = new
        self.length += 1
        
    def __repr__(self):
        result = ''
        curr = self.head
        while curr.nxt:
            result += str(curr.value) + ' '
            curr = curr.nxt
        result += str(curr.value)
        return result

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    first = Node(tmp[0])
    prog = LinkedList(first)    # Initialize Linked list
    for i in range(0, n-1):
        prog.insert(i, Node(tmp[i]))
    for _ in range(m-1):
        tmp = list(map(int, input().split()))
        # Find larger value than tmp[0]
        first = tmp[0]
        insert_idx = -1
        for i in range(prog.length):
            if prog.get(i) > first:
                insert_idx = i
                break
        if insert_idx == 0:
            prog.appendleft()
        
    
    print('#{} {}'.format(test_case, prog))

print(time.time() - start, 's')