import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt

    def __repr__(self):
        return str(self.val)

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, val):
        if self.length == 0:
            new = Node(val)
            self.head = new
            self.tail = new
        else:
            curr = self.tail
            new = Node(val, curr)
            curr.nxt = new
            self.tail = new
        
        self.length += 1

    def search(self, idx):
        curr_idx = 0
        curr = self.head
        if curr == None and idx != 0:
            return -1
        while curr_idx < idx:
            curr_idx += 1
            if curr.nxt == None:
                return -1
            curr = curr.nxt
        return curr

    def insert(self, idx, val):
        curr = self.search(idx)
        if curr == -1:
            raise IndexError
        new = Node(val, curr.pre, curr)
        if idx == 0:
            self.head = new
        else:
            curr.pre.nxt = new

        self.length += 1
    
    def delete(self, idx):
        curr = self.search(idx)
        if curr == -1:
            raise IndexError
        if idx == 0:    # 맨 앞 노드
            self.head = curr.nxt
            curr.nxt.pre = None
            curr.nxt = None
        elif curr.nxt == None:  # 맨 뒤 노드
            self.tail = curr.pre
            curr.pre.nxt = None
            curr.pre = None
        else:
            curr.pre.nxt = curr.nxt
            curr.nxt.pre = curr.pre
        
        del curr
        self.length -= 1

    def change(self, idx, val):
        curr = self.search(idx)
        if curr == -1:
            raise IndexError
        curr.val = val

    def __repr__(self):
        curr = self.head
        result = str(curr.val)
        while curr.nxt:
            curr = curr.nxt
            result += ' ' + str(curr.val)
        return result

t = int(input())
for test_case in range(1, t+1):
    # 수열의 길이, 편집 횟수, 출력할 인덱스
    n, m, l = map(int, input().split())
    seq = input().split()
    dll = DoubleLinkedList()
    for num in seq:
        dll.append(num)

    for _ in range(m):
        cmd, *num = input().split()
        if cmd == 'I':
            dll.insert(int(num[0]), num[1])
        elif cmd == 'D':
            dll.delete(int(num[0]))
        elif cmd == 'C':
            dll.change(int(num[0]), num[1])

    result = dll.search(l)
    if result != -1:
        result = result.val
    print('#{} {}'.format(test_case, result))
