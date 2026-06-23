# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(n: Optional[TreeNode]) -> int:
            if n == None:
                return 0
            l = 1 + dfs(n.left)
            r = 1 + dfs(n.right)
            return max(l, r)
        return dfs(root)