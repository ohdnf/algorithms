import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self, arr):
        """
        This linked-list needs an array to init an instance.
        Each single element in the array will be linked in order.
        """
        self.head = Node(arr[0])
        before = self.head
        for i in range(1, len(arr)):
            curr = Node(arr[i])
            before.nxt = curr
            before = curr

    def insert(self, idx):
        """
        Insert new node in the specified index.
        Value of the new node will be a sum of value of pre- and post-node.
        """
        curr = self.head
        curr_idx = 0

        while curr_idx < idx:
            curr = curr.nxt
            curr_idx += 1
        
        insert_val = 0
        if curr.nxt:      # Insert middle
            insert_val = curr.val + curr.nxt.val
        else:               # Insert last
            insert_val = curr.val + self.head.val
        new = Node(insert_val)
        new.nxt = curr.nxt
        curr.nxt = new
    
    def __repr__(self):
        """
        Print only 10 values of each node in descending order.
        """
        result = list()
        curr = self.head
        result.append(str(curr.val))
        while curr.nxt:
            curr = curr.nxt
            result.append(str(curr.val))
        return ' '.join(result[-1:-11:-1])


t = int(input())
for test_case in range(1, t+1):
    n, m, k = map(int, input().split())
    numbers = LinkedList(list(map(int, input().split())))
    idx = 0
    for _ in range(k):
        # Select an index before the index in which new node will be inserted
        idx += m - 1
        if idx > n - 1:
            idx -= n
        numbers.insert(idx)
        idx += 1
        n += 1

    print('#{} {}'.format(test_case, numbers))