# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""
        def get_num_string(h: Optional[ListNode]) -> int:
            n = ""
            t = h
            while t is not None:
                n += str(t.val)
                t = t.next
            return int(n[::-1])
        n1 = get_num_string(l1)
        n2 = get_num_string(l2)
        ans_str = str(n1+n2)[::-1]
        print(f"{n1=} {n2=} {n1+n2=} {ans_str=}")

        new_h = ListNode(int(ans_str[0]), None)
        t = new_h
        for i in range(1, len(ans_str)):
            c = ListNode(int(ans_str[i]), None)
            t.next = c
            t = t.next
        return new_h