import sys
sys.stdin = open('input.txt')

class Node:
    # def __init__(self, val, pre=None, nxt=None):
    def __init__(self, val, nxt=None):
        self.val = val
        # self.pre = pre
        self.nxt = nxt
    
    def __repr__(self):
        return f'{self.val}'

class LinkedList:
    def __init__(self, node=None):
        self.head = node
    
    def append(self, val):
        curr = self.head
        if curr is None:
            self.head = Node(val)
            return
        while curr.nxt:
            curr = curr.nxt
        # curr.nxt = Node(val, curr)
        curr.nxt = Node(val)
        return
    
    def insert(self, idx, val):
        curr_idx = 0
        curr = self.head
        # while curr_idx < idx:
        while curr_idx < idx-1:
            curr_idx += 1
            curr = curr.nxt
        # new = Node(val, curr.pre, curr)
        target = curr.nxt
        curr.nxt = Node(val, target)
        # curr.pre.nxt = new
        # curr.pre = new
        return
    
    def delete(self, idx):
        curr_idx = 0
        curr = self.head
        # while curr_idx < idx:
        while curr_idx < idx-1:
            curr_idx += 1
            curr = curr.nxt
        curr.nxt = curr.nxt.nxt
        # if idx == 0:
        #     if curr.nxt:
        #         self.head = curr.nxt
        #         curr.nxt.pre = None
        #     else:
        #         self.head = None
        # else:
        #     if curr.nxt:
        #         curr.pre.nxt = curr.nxt
        #         curr.nxt.pre = curr.pre
        #     else:
        #         curr.pre.nxt = None
        del curr
        return

    def change(self, idx, val):
        curr_idx = 0
        curr = self.head
        while curr_idx < idx:
            curr_idx += 1
            curr = curr.nxt
        curr.val = val
        return
    
    def index(self, idx):
        curr_idx = 0
        curr = self.head
        while curr is not None and curr_idx < idx:
            curr_idx += 1
            curr = curr.nxt
        if curr is None:
            return -1
        else:
            return curr.val
    
    def __repr__(self):
        curr = self.head
        if curr == None:
            return 'None'
        output = str(curr.val)
        while curr.nxt:
            curr = curr.nxt
            output += '-' + str(curr.val)
        return output


t = int(input())
for test_case in range(1, t+1):
    # 수열의 길이, 편집 횟수, 출력할 인덱스
    n, m, l = map(int, input().split())
    seq = input().split()
    linkedList = LinkedList()
    for e in seq:
        linkedList.append(e)
    # print(linkedList)

    for _ in range(m):
        cmd, *num = input().split()
        # print(cmd, *num)
        if cmd == 'I':
            linkedList.insert(int(num[0]), num[1])
        elif cmd == 'D':
            linkedList.delete(int(num[0]))
        elif cmd == 'C':
            linkedList.change(int(num[0]), num[1])
        # print(linkedList)
    
    result = linkedList.index(l)
    print('#{} {}'.format(test_case, result))
