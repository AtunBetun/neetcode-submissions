# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = head
        l = 0
        while t is not None:
            t = t.next
            l += 1

        if l == 1:
            return None
            
        c = l - n
        t = head
        p = head

        if c == 0:
            return head.next

        print(f"{l=} {c=}")
        for i in range(0, c):
            p = t
            t = t.next

        p.next = t.next
        t.next = None
        print(f"{t.val=} {p.val=}")
        return head
