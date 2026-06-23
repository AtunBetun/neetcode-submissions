# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(n: Optional[TreeNode]) -> int:
            nonlocal ans
            if not n:
                return 0

            l = dfs(n.left)
            r = dfs(n.right)
            ans = max(ans, l + r)
            return 1 + max(l, r)
        dfs(root)
        return ans