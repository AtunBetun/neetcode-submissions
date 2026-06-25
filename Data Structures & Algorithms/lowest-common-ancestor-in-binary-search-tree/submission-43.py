# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None
        def dfs(n):
            nonlocal ans
            if n is None:
                return ""
            l = dfs(n.left)
            r = dfs(n.right)
            c = l + r
            if n.val == p.val:
                c += "p"
            if n.val == q.val:
                c += "q"
            print(f"{n.val=} {c=}")
            c = "".join(sorted(c))
            if c == "pq":
                if ans is None:
                    ans = n
            return c
        dfs(root)
        return ans