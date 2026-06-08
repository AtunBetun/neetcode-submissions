# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverseList(head):
            if head is None or head.next is None:
                return head
        
            # reverse the rest of linked list and put the 
            # first element at the end
            rest = reverseList(head.next)
        
            # Make the current head as last node of 
            # remaining linked list
            head.next.next = head
        
            # Update next of current head to NULL
            head.next = None
        
            # Return the reversed linked list
            return rest

        return reverseList(head)