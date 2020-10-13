# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 내 풀이
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            output = head
            head = nxt
        return output
    
    # 반복 구조 깔끔 풀이
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev
    
    # 재귀 구조
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)