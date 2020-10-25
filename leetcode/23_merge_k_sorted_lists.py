from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        total = []
        for head in lists:
            while head:
                total.append(head.val)
                head = head.next
        total.sort()
        merged_list = head = ListNode()
        for num in total:
            head.next = ListNode(num)
            head = head.next
        return merged_list.next
