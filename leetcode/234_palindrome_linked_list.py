from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    # 리스트로 변환
    def isPalindrome(self, head: ListNode) -> bool:
        string = []
        curr = head
        while curr:
            string.append(curr.val)
            curr = curr.next
        return string == string[::-1]
    
    # Runner 기법
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # Runner를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # 전체 길이가 홀수일 경우 처리
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev


"""
Runner 기법

연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
Fast Runner는 두 칸씩, Slow Runner는 한 칸씩 이동하게 하면,
Fast Runner가 연결 리스트의 끝에 도달할 때 
Slow Runner가 정확히 연결리스트의 중간 지점을 가리키게 된다.

이와 같은 방식으로 중간 위치나 병합 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
"""