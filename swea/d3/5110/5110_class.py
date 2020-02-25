import sys
sys.stdin = open('input.txt')
import time
start = time.time()

class Node:
    def __init__(self, value, pre=None, nxt=None):
        self.value = value
        self.pre = pre
        self.nxt = nxt

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node

    def append(self, node):
        node.pre = self.tail
        self.tail.nxt = node
        self.tail = node
    
    def insert(self, target, linkedList):
        if target.nxt != None:
            front = target.pre
            back = target.nxt
            linkedList.head.pre = front
            front.nxt = linkedList.head
            linkedList.tail.nex = back
            back.pre = linkedList.tail
            self.tail = linkedList.tail
        else:
            target.nxt = linkedList.head
            linkedList.head.pre = target
    
    def find(self, value):
        curr = self.head
        while curr.nxt:
            if curr.value > value:
                return curr
            else:
                curr = curr.nxt
        return curr
    
    def index(self, value):
        curr = self.head
        idx = 0
        while curr.nxt:
            if curr.value == value:
                return
    
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
    first = tmp[0]
    prog = LinkedList(Node(first))
    for i in range(1, n):
        prog.append(Node(tmp[i]))
    for _ in range(m):
        tmp = list(map(int, input().split()))
        first = tmp[0]
        incoming = LinkedList(Node(first))
        for i in range(1, n):
            incoming.append(Node(tmp[i]))
        target = prog.find(first)
        prog.insert(target, incoming)        
    
    print('#{} {}'.format(test_case, prog))

print(time.time() - start, 's')