"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        t = head
        d = {}

        print(f"original")
        while t is not None:
            print(f"{t.val=}")
            t = t.next

        new_h = Node(head.val)
        new_t = new_h
        t = head
        while t is not None:
            if t.next is not None: # create next node
                c = Node(t.next.val, None, None)
                new_t.next = c
            d[t] = (t, new_t)
            t = t.next
            new_t = new_t.next
        
        print(f"\nnew")
        t = head
        while t is not None:
            print(f"{t.val=}")
            if t.random is not None:
                print(f"random: {t.val=} {t.random.val=}")
                d[t][1].random = d[t.random][1]
            t = t.next
        return new_h