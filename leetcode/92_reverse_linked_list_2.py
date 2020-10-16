# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m - 1):
            start = start.next

        end = start.next

        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next

    # 다른 풀이
    def reverseBetween1(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = dummy_head = ListNode()
        dummy.next = head
        for _ in range(m - 1):
            dummy = dummy.next
        itr = dummy.next
        for _ in range(n - m):
            temp = itr.next
            dummy.next, temp.next, itr.next = temp, dummy.next, temp.next
        return dummy_head.next


# 재귀
"""
Algorithm
1. We define a recursion function that will do the job of reversing a portion of the linked list.
연결 리스트의 부분을 뒤집을 재귀 함수를 선언합니다.

2. Let's call this function `recurse`. The function takes in 3 parameters: 
`m` being the starting point of the reversal, `n` being the ending point for the reversal, 
and a pointer `right` which will start at the nth node in the linked list and move backwards 
with the backtracking of the recursion. If this is not clear at the moment, the diagrams that follow will help.
이 함수를 `recurse`라 명합니다. 함수는 3개 인자를 갖습니다:
`m`은 뒤집힐 연결 리스트의 시작 지점이고, `n`은 마지막 지점, 그리고 `right` 포인터는 연결 리스트의 n번째 노드에서부터
시작하여 재귀로 백트래킹할 때마다 왼쪽으로 한 칸씩 옮겨갑니다.

3. Additionally, we have a pointer called `left` which starts from the mth node in the linked list and moves forward. 
In Python, we have to take a global variable for this which get's changed with recursion. 
In other languages, where changes made in function calls persist, we can consider this pointer 
as an additional variable for the function `recurse`.
추가적으로, `left` 포인터는 m번째 노드에서 시작해 오른쪽으로 이동합니다. 파이썬에서는 전역 변수로 설정해 재귀할 때
값이 변하도록 합니다. 함수 호출 시 변화가 반영되는 다른 언어에서는 이 포인터를 `recurse` 함수의 추가 변수로 
생각할 수 있습니다. 

4. In a recursion call, given `m`, `n`, and `right`, we check if `n == 1`. If this is the case, 
we don't need to go any further.
재귀 호출에서 `m`, `n`, 그리고 `right`가 주어졌을 때 `n == 1` 조건을 확인합니다. 조건을 충족한다면 재귀를 멈추고 
백트래킹을 시작합니다.

5. Until we reach `n = 1`, we keep moving the `right` pointer one step forward and after doing that, 
we make a recursive call with the value of n decreased by 1. At the same time, we keep on moving the 
`left` pointer forward until `m == 1`. When we refer to a pointer being moved forward, 
it essentially means `pointer.next`.
`n = 1`에 도달하기 전, `right` 포인터를 왼쪽으로 한 노드씩 이동시키며 값을 1씩 감소하여 재귀 호출합니다. 동시에, 
`left` 포인터를 `m == 1` 조건을 만족하기 전까지 오른쪽으로 이동시킵니다. 여기서 포인터가 왼쪽으로 이동한다는 것은, 
다음 노드인 `pointer.next`를 가리키는 것을 말합니다.

6. So we backtrack as soon as `n` reaches 1. At that point of time, the `right` pointer is at the last node 
of the sublist we want to reverse and the `left` has already reached the first node of this sublist. So, we swap out 
the data and move the left pointer one step forward using `left = left.next`. We need this change to 
persist across the backtracking process.
`n`이 1에 도달하는 순간 백트래킹을 시작합니다. 이 순간, `right` 포인터는 역순으로 뒤집을 부분 리스트의 맨 오른쪽에 
위치하며, `left` 포인터는 이미 부분 리스트의 첫 번째 노드에 위치하고 있습니다. 따라서, 데이터를 교체하며 
`left = left.next`로 `left` 포인터를 오른쪽으로 한 노드씩 이동시킵니다. 백트래킹을 하며 이 과정을 반복합니다.

7. From there on, every time we backtrack, the `right` pointer moves one step backwards. 
This is the simulation we've been mentioning all along. The backward movement is simulated by backtracking.
동시에 `right` 포인터도 왼쪽으로 한 노드씩 이동합니다.

8. We stop the swaps when either `right == left`, which happens if the sublist size is odd, or, `right.next == left` 
which happens when during the backtracking process for an even sized sublist, the `right` pointer crosses left. 
We use a global boolean flag for stopping the swaps once these conditions are met.
두 노드의 교체는 리스트의 길이가 홀수일 때 `right == left`가 되거나, 리스트의 길이가 짝수일 때 `right` 포인터가 
`left` 포인터를 지나치며 `right.next == left` 조건을 만족할 때 멈춥니다. 참거짓 전역 변수를 사용해 해당 조건들이 
성립될 때 교체들이 종료될 수 있게 합니다. 
"""


class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head
