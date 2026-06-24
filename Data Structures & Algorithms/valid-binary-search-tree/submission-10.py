# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n: Optional[TreeNode], l: int, h: int) -> bool:
            if n is None:
                return True
            print(f"{n.val=} {l=} {h=}")

            # check next nodes
            if n.left and n.left.val >= n.val:
                return False
            elif n.right and n.right.val < n.val:
                return False

            # check branch mins / max
            if n.val >= l:
                return False
            if n.val <= h:
                return False

            return dfs(n.left, min(l, n.val), h) and dfs(n.right, l, max(h, n.val))
        return dfs(root, 2000, -2000) # set correct mins and high
