class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt
    
    def __repr__(self):
        return f'{self.val}'


class LinkedList:
    def __init__(self, node):
        self.head = node

    def read(self, idx):
        curr = self.head
        curr_idx = 0
        while curr_idx < idx:
            if curr.nxt == None:
                raise IndexError
            curr = curr.nxt
            curr_idx += 1
        return curr.val
    
    def index(self, val):
        curr = self.head
        curr_idx = 0
        while curr:
            if val == curr.val:
                return curr_idx
            else:
                curr = curr.nxt
                curr_idx += 1
        return None

    def insert(self, idx, val):
        curr = self.head
        curr_idx = 0

        while curr_idx < idx:
            curr = curr.nxt
            curr_idx += 1
        
        new = Node(val)
        new.nxt = curr.nxt
        curr.nxt = new

    def delete(self, idx):
        curr = self.head
        curr_idx = 0
        
        while curr_idx < idx - 1:
            curr = curr.nxt
            curr_idx += 1
        
        node_after_deleted_node = curr.nxt.nxt
        curr.nxt = node_after_deleted_node

    def __repr__(self):
        curr = self.head
        values = [str(curr.value)]
        while curr.nxt:
            curr = curr.nxt
            values.append(str(curr.value))
        return ' '.join(values)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n1.nxt = n2
    n3 = Node(3)
    n2.nxt = n3
    n4 = Node(4)
    n3.nxt = n4
    l1 = LinkedList(n1)
    print(l1)
    print(l1.read(0))
    print(l1.index(3))