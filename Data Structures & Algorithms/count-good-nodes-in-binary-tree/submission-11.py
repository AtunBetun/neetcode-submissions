# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        def check(node, seen):
            if seen == []:
                return True
            for x in seen:
                if x > node.val:
                    return False
            return True
        def dfs(node, seen) -> None:
            if node is None:
                return
            
            print(f"CURR: {node.val=} {seen=}")
            curr = check(node, seen)
            if curr:
                print(f"found {node.val=}")
                ans[0] += 1
            seen.append(node.val) # see node
            left = dfs(node.left, seen)
            right = dfs(node.right, seen)
            seen.pop()
            return 
        dfs(root, [])
        return ans[0]

        