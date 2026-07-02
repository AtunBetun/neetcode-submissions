"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        n = deque([node])
        d = {}
        d[node] = Node(node.val)
        while n:
            t = n.popleft()
            for x in t.neighbors:
                if x not in d:
                    n.append(x)
                    d[x] = Node(x.val)
                d[t].neighbors.append(d[x])
        return d[node]