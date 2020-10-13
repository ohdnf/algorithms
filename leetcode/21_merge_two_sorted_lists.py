# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # iteratively
    def mergeTwoLists1(self, l1:ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    # recursively
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if (not l1) or (l2 and (l1.val > l2.val)):    <== 연산 순서
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    
    # recursively 2
    def mergeTwoLists2_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # in-place, iteratively
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        dummy = curr = ListNode()
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                # l2.val만 쏙 빼가기
                nxt = curr.next     # l1.next
                curr.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next