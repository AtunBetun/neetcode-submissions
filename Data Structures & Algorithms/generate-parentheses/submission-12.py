class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(open_l: int, close_l: int, s: str) -> None:
            print(f"{open_l=} {close_l=} {s=}")
            # no more moves
            if open_l == 0 and close_l == 0:
                print(f"found {s=}")
                res.append(s)
                return 

            # more moves to do
            if open_l > 0:
                print("left move")
                helper(open_l - 1, close_l, s + '(')
            
            if close_l > open_l:
                helper(open_l, close_l - 1, s + ')')

        helper(n, n, '')
        print(f"{res=}")
        return res


