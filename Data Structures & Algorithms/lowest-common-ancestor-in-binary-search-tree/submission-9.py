# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # DFS, return boolean
        # True if p or q was found, False otherwise
        # post-order, check in global variable if we are lower
        print(f"{p.val=} {q.val=}")
        ans = []
        def dfs(node):
            if node is None:
                return False
            print(f"{node.val=}")

            curr = (node.val == p.val or node.val == q.val)
            left = dfs(node.left)
            right = dfs(node.right)

            if (
                left and right
                or curr and left
                or curr and right
            ):
                print(f"found {node.val=}")
                ans.append(node)

            return left or right or curr
        dfs(root)
        ans.sort(key=lambda x: x.val)
        return ans[0]
            
        