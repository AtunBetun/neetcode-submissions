# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(n) -> int:
            nonlocal ans
            if n is None:
                return 0
            l = 1 + dfs(n.left)
            r = 1 + dfs(n.right)
            diff = abs(l - r)
            if diff > 1:
                ans = False
            return max(l, r)
        dfs(root)
        return ans