# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            if node is None or node.next is None: # base case
                return node
            
            rest = reverse(node.next) # returns 5

            node.next.next = node
            node.next = None

            return rest
        return reverse(head)





