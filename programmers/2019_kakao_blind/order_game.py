from collections import deque as dq
import sys

sys.setrecursionlimit(10**5)


class Node:
    def __init__(self, value, x, left=None, right=None):
        self.value = value
        self.x = x
        self.left = left
        self.right = right
    
    def adopt(self, node):
        if node.x < self.x:
            if self.left:
                self.left.adopt(node)
            else:
                self.left = node
        elif self.x < node.x:
            if self.right:
                self.right.adopt(node)
            else:
                self.right = node
    
    def __repr__(self):
        return f'Value: {self.value}'

class Tree:
    def __init__(self, node):
        self.head = node
        self.visit_order = list()
    
    def insert(self, node):
        self.head.adopt(node)
    
    def order(self, cmd):
        self.visit_order = list()
        if cmd == 'pre':
            self.preorder(self.head)
        elif cmd == 'post':
            self.postorder(self.head)
        return self.visit_order

    def preorder(self, node):
        if node:
            self.visit_order.append(node.value)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            self.visit_order.append(node.value)

    def __repr__(self):
        string = 'level 0: '
        self.queue = dq()
        self.queue.append((self.head, 0))
        level_before = 0
        while self.queue:
            curr, level = self.queue.popleft()

            if level == level_before:
                string += str(curr) + ' '
            else:
                string += f'\nlevel {level}: ' + str(curr) + ' '
                level_before = level

            if curr.left:
                self.queue.append((curr.left, level+1))
            if curr.right:
                self.queue.append((curr.right, level+1))
        
        return string

def solution(node_info):
    location = list()
    left = 100000
    right = 0
    for idx, node in enumerate(node_info):
        x, y = node
        location.append([idx+1, x, y])
        if right < x:
            right = x
        if x < left:
            left = x
    
    location.sort(key=lambda node: (-node[2], node[1]))

    root = location.pop(0)
    tree = Tree(Node(root[0], root[1]))
    for node in location:
        val, x, _ = node
        tree.insert(Node(val, x))
    
    pre_order = tree.order('pre')
    post_order = tree.order('post')

    return [pre_order, post_order]


if __name__ == "__main__":
    # nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    nodeinfo = [[i,i] for i in range(1000)]
    print(solution(nodeinfo))
