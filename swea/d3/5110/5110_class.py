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
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0
    
    def append(self, val):
        if self.head is None:   # 빈 리스트일 경우
            new = Node(val)
            self.head = new
            self.tail = new
        else:
            curr = self.head
            while curr.nxt:
                curr = curr.nxt
            new = Node(val, curr)
            curr.nxt = new
            self.tail = new
        self.length += 1
        return
    
    def extend(self, linkedList):
        first = linkedList.head # 삽입할 수열의 첫 번째 노드
        last = linkedList.tail  # 삽입할 수열의 마지막 노드
        self.length += linkedList.length    # 길이 추가
        # 노드 탐색
        curr = self.head
        curr_idx = 0
        while curr_idx < self.length:
            if curr.val > first.val:
                # 현재 노드 앞에 수열 끼워 넣기
                first.pre = curr.pre
                last.nxt = curr
                curr.pre.nxt = first
                curr.pre = last
                if curr_idx == 0:
                    self.head = first
                return
            curr = curr.nxt
            curr_idx += 1
        # 맨 뒤에 수열 붙이기
        first.pre = curr
        curr.nxt = first
        self.tail = last
    
    def index(self, idx):
        curr = self.head
        curr_idx = 0
        while curr_idx < idx:
            curr = curr.nxt
            curr_idx += 1
        return curr
    
    def get_last_ten(self):
        result = list()
        curr = self.tail
        while len(result) < 10:
            result.append(curr.val)
            curr = curr.nxt
        return result

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
    data = list(map(int, input().split()))
    seq = LinkedList()
    for datum in data:
        seq.append(datum)
    for _ in range(m-1):
        data = list(map(int, input().split()))
        incoming = LinkedList()
        for datum in data:
            incoming.append(datum)
        seq.extend(incoming)
    result = seq.get_last_ten()
    print('#{} {}'.format(test_case, *result))

print(time.time() - start, 's')