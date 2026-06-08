# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [None]

        def dfs(node, idx):
            if not node or ans[0] is not None:
                return idx  # return current index if null or already found

            idx = dfs(node.left, idx)

            idx += 1  # visiting this node
            if idx == k:
                ans[0] = node.val
                return idx  # return immediately to stop recursion

            idx = dfs(node.right, idx)

            return idx  # propagate index up the stack

        dfs(root, 0)
        return ans[0]
