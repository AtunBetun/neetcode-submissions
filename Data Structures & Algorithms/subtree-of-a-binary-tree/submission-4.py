# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        def is_tree_equal(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if n1 == None and n2 == None:
                return True
            
            if (
                (n1 == None and n2 != None)
                or (n1 != None and n2 == None)
            ):
                return False
            elif (
                n1 != None and n2 != None
                and n1.val != n2.val
            ):
                return False
            return is_tree_equal(n1.left, n2.left) and is_tree_equal(n1.right, n2.right)

        def dfs(n: Optional[TreeNode]) -> bool:
            if n is None:
                return False

            sub = False
            if n.val == subRoot.val: # found initial subtree
                sub = is_tree_equal(n, subRoot)

            return dfs(n.left) or dfs(n.right) or sub
        return dfs(root)
            