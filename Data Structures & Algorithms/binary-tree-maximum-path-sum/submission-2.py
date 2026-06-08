# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float('-inf')]

        # DFS
        # highest possible sum of A branch, not both
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            print(f"{node.val=} {left=} {right=}")
            branch_sum = max(
                node.val,
                node.val + left,
                node.val + right
            )
            global_sum = max(
                node.val, 
                node.val + left, 
                node.val + right, 
                node.val + left + right
            )
            ans[0] = max(global_sum, ans[0])

            return branch_sum
        dfs(root)
        return ans[0]
