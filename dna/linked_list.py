class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt
    
    def __repr__(self):
        return f'{self.value}'


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
        return curr.value

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