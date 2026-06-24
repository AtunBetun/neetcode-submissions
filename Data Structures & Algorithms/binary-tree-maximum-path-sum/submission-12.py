# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(n: Optional[TreeNode]) -> int:
            nonlocal ans
            if n is None:
                return 0

            l = dfs(n.left)
            r = dfs(n.right)

            s = max(n.val+l+r, n.val+l, n.val+r, n.val) # only pick the best path
            ans = max(s, ans)
            return max(n.val+l, n.val+r, n.val)
        dfs(root)
        return ans