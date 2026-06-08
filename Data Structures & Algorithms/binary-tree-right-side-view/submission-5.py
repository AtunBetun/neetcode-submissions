# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        que = deque([(root, 0)]) # starting
        ans = {}
        while que:
            node, depth = que.popleft()
            if node is None:
                continue
            if depth not in ans:
                ans[depth] = []
            ans[depth].append(node.val)
            que.append((node.left, depth+1))
            que.append((node.right, depth+1))
        final = []
        for x in ans.values():
            final.append(x[-1])
        return final



