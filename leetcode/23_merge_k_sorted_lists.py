from typing import List
import heapq


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

    def mergeKLists_heapq(self, lists: List[ListNode]) -> ListNode:
        root = curr = ListNode()
        heap = []

        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx, head))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            curr.next = node[2]

            curr = curr.next
            if curr.next:
                heapq.heappush(heap, (curr.next.val, idx, curr.next))

        return root.next
