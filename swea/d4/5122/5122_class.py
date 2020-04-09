import sys
sys.stdin = open('input.txt')
# sys.stdin = open('swea/d4/5122/input.txt')
class Node:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt
    
    def __repr__(self):
        return f'{self.val}'

class LinkedList:
    def __init__(self, val=None):
        if val == None:
            self.head = val
            self.tail = val
        else:
            new = Node(val)
            self.head = new
            self.tail = new
    
    def append(self, val):
        curr = self.tail
        new = Node(val)
        if curr == None:
            self.head = new
        else:
            curr.nxt = new
            new.pre = curr
        self.tail = new
    
    def insert(self, idx, val):
        # 추가할 인덱스 위치의 노드 찾기
        curr_idx = 0
        curr = self.head
        if curr == None and idx != 0:
            raise IndexError
        while curr_idx < idx:
            curr_idx += 1
            if curr.nxt == None:
                raise IndexError
            curr = curr.nxt
        new = Node(val) # 새로 추가할 노드
        if idx == 0:    # 맨 앞에 추가
            new.nxt = curr
            curr.pre = new
            self.head = new
        else:
            node_before = curr.pre
            new.pre = node_before
            new.nxt = curr
            node_before.nxt = new
            curr.pre = new
    
    def index(self, idx):
        curr_idx = 0
        curr = self.head
        if curr == None and idx != 0:
            return -1
        while curr_idx < idx:
            curr_idx += 1
            if curr.nxt == None:
                return -1
            curr = curr.nxt
        return curr.val
    
    def delete(self, idx):
        curr_idx = 0
        curr = self.head
        if curr == None and idx != 0:
            raise IndexError
        while curr_idx < idx:
            curr_idx += 1
            if curr.nxt == None:
                raise IndexError
            curr = curr.nxt
        
        if idx == 0 or curr.pre == None:    # 맨 앞 노드 삭제
            node_next = curr.nxt
            node_next.pre = None
            self.head = node_next
        elif curr.nxt == None:  # 맨 뒤 노드 삭제
            node_before = curr.pre
            node_before.nxt = None
            self.tail = node_before
        else:   # 중간 노드 삭제
            node_before = curr.pre
            node_next = curr.nxt
            # 앞 노드와 뒤 노드 연결
            node_before.nxt = node_next
            node_next.nxt = node_before
        del curr
    
    def change(self, idx, val):
        curr_idx = 0
        curr = self.head
        if curr == None and idx != 0:
            raise IndexError
        while curr_idx < idx:
            curr_idx += 1
            if curr.nxt == None:
                raise IndexError
            curr = curr.nxt
        curr.val = val

    def __repr__(self):
        result = '['
        curr = self.head
        while curr.nxt:
            result += str(curr.val) + ', '
            curr = curr.nxt
        result += ']'
        return f'{result}'


t = int(input())
for test_case in range(1, t+1):
    n, m, l = map(int, input().split())
    data = list(map(int, input().split()))
    # linked-list 만들기
    link = LinkedList()
    for datum in data:
        link.append(datum)
    for _ in range(m):
        cmd, *num = input().split()
        if cmd == 'I':
            link.insert(int(num[0]), num[1])
        elif cmd == 'D':
            link.delete(int(num[0]))
        elif cmd == 'C':
            link.change(int(num[0]), num[1])
    result = link.index(l)
    print('#{} {}'.format(test_case, result))