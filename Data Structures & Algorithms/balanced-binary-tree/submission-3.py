# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS
        # Return the depth of tree
        # Global var to update after each recursion
        ans = [True]
        def dfs(node):
            if node is None:
                return 0 # no depth

            left = dfs(node.left)
            right = dfs(node.right)
            if max(left, right) - min(left, right) > 1:
                ans[0] = False
            return 1 + max(left, right)
        dfs(root)
        return ans[0]

