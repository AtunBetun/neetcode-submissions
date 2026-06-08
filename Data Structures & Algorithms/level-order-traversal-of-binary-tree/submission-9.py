# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = {}
        que = deque([(root, 0)]) # starting

        while que: # BFS
            node, depth = que.popleft() # tuple
            if node is None:
                continue
            if depth not in ans:
                ans[depth] = [] # initialize
            ans[depth].append(node.val)
            que.append((node.left, depth+1))
            que.append((node.right, depth+1))
        print(f"{ans.values()=}")
        final_ans = []
        for x in ans.values():
            final_ans.append(x)
        return final_ans


        

        