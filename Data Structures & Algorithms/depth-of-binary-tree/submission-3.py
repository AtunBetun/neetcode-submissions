# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(n: Optional[TreeNode]) -> int:
            if n == None:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            return 1 + max(l, r)
        return dfs(root)