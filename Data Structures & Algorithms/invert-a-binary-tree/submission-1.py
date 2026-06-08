# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs on nodes
        # pre-node traversal => visit node BEFORE recursing
        # swap values
        # recurse
        # O(n)

        def dfs(n):
            if n is None:
                return
            temp = n.left
            n.left = n.right
            n.right = temp
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return root