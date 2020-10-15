from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next:
            return f'{self.val}->'
        else:
            return f'{self.val}->NULL'


# 나의 풀이
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = odd = ListNode()
        even_head = even = ListNode()
        idx = 0
        while head:
            if idx % 2:
                even.next = ListNode(head.val)
                even = even.next
            else:
                odd.next = ListNode(head.val)
                odd = odd.next

            idx += 1
            head = head.next

        odd.next = even_head.next

        return odd_head.next


# 다른 풀이
class Solution2:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head


if __name__ == '__main__':
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    s = Solution()
    linked_list = s.oddEvenList(one)
    print(linked_list)
