# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS on the tree
        # find heights of both trees
        # ans global for diameter
        ans = [0]
        def dfs(node): # returns heights
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans[0] = max(ans[0], left + right)
            return 1 + max(left, right)
        dfs(root)
        return ans[0]