# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l = ""
        def dfs(n):
            nonlocal l
            if n is None:
                print("null")
                l += ",null"
                return
            print(n.val)
            l += f",{str(n.val)}"
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return l[1:]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        a = data.split(",")
        for i in range(0, len(a)):
            if a[i] == "null":
                a[i] = None
            else:
                a[i] = int(a[i])   

        i = 0
        # stack approach to keep last node
        def dfs() -> Optional[TreeNode]:
            nonlocal i
            if a[i] == None:
                i += 1
                return None

            node = TreeNode(a[i])
            i += 1

            node.left = dfs()
            node.right = dfs()
            return node
        print(f"{a=}")
        return dfs()