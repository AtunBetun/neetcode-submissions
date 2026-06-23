# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(n: Optional[TreeNode]) -> Optional[TreeNode]:
            if n is None:
                return None
            t = n.left
            n.left = n.right
            n.right = t
            dfs(n.left)
            dfs(n.right)
        h = root
        dfs(h)
        return root