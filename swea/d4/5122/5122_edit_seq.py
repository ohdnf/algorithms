import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt
    
    def set(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

class DoubleLinkedList:
    def __init__(self, arr):
        self.head = Node(arr[0])
        curr = self.head
        self.length = 1
        for i in range(1, len(arr)):
            new = Node(arr[i], curr)
            curr.nxt = new
            curr = new
            self.length += 1
    
    def search(self, idx):
        curr = self.head
        curr_idx = 0
        while curr_idx < idx:
            if curr == None:
                return None
            curr = curr.nxt
            curr_idx += 1
        return curr

    def insert(self, idx, val):
        target = self.search(idx)
        if idx == 0:
            new = Node(val)
            target.pre = new
            new.nxt = target
            self.head = new
        else:
            new = Node(val, target.pre, target)
            target.pre.nxt = new
            target.pre = new
        
        self.length += 1
    
    def delete(self, idx):
        target = self.search(idx)
        if idx == 0:
            self.head = target.nxt
            self.head.pre = None
        elif target.nxt == None:
            target.pre.nxt = None
        else:
            target.pre.nxt = target.nxt
            target.nxt.pre = target.pre
        
        del target
        
        self.length -= 1

    def change(self, idx, val):
        target = self.search(idx)
        target.set(val)

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
    seq = DoubleLinkedList(list(input().split()))

    for _ in range(m):
        cmd, *num = input().split()
        if cmd == 'I':
            seq.insert(int(num[0]), num[1])
        elif cmd == 'D':
            seq.delete(int(num[0]))
        elif cmd == 'C':
            seq.change(int(num[0]), num[1])

    # result = seq.search(l)
    # if result:
    #     result = result.val
    # else:
    #     result = -1
    
    result = -1
    if l < seq.length:
        result = seq.search(l).val
    print('#{} {}'.format(test_case, result))

