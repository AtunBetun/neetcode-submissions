# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive approach


        def merge(node1, node2):
            if (
                node1 is None
                or node2 is None
            ):
                print(f"BASE CASE")
                return node1 or node2
            
            if (node1.val <= node2.val):
                node1.next = merge(node1.next, node2)
                return node1
            else:
                node2.next = merge(node1, node2.next)
                return node2
            
        return merge(list1, list2)

