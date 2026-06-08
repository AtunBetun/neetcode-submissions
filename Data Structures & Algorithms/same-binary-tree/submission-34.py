# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preOrderT(n: Optional[TreeNode], arr: List[int | None]):
            if n is None:
                print(f"n.val is None")
                arr.append(None)
                return

            arr.append(n.val)
            preOrderT(n.left, arr)
            print(f"{n.val=}")
            preOrderT(n.right, arr)

        t1Arr = []
        t2Arr = []
        print("\nleft")
        preOrderT(p, t1Arr)

        print("\nright")
        preOrderT(q, t2Arr)
        print(f"{t1Arr=} {t2Arr=}")
        return t1Arr == t2Arr