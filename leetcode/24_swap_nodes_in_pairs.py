# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 반복
    def swapPairs(self, head: ListNode) -> ListNode:
        output = prev = ListNode()
        prev.next = head

        while head and head.next:
            second = head.next
            head.next = second.next
            second.next = head

            prev.next = second

            head = head.next
            prev = prev.next.next

        return output.next

    # 재귀
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head

