class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getBox(r: int, c: int) -> int:
            return (r // 3) * 3 + (c // 3)

        def check(x: List[str]) -> bool:
            count = Counter(x)
            for x in count.items():
                if x[0] == '.':
                    continue
                if int(x[0]) < 0 or int(x[0]) > 9:
                    return False
                if int(x[1]) > 1:
                    return False
            return True

        ans = True
        d = defaultdict(list)
        for x in range(0, 9):
            d[('box', x)] = []
            d[('col', x)] = []

        for r in range(0, 9):
            for c in range(0, 9):
                box = getBox(r, c)
                print(f"{r=} {c=} {box=}")
                ans = ans and check(board[r])
                if not ans:
                    return False
                d[('col', c)].append(board[r][c])
                d[('box', box)].append(board[r][c])
        for x in list(d.items()):
            ans = ans and check(x[1])
            if not ans:
                return False

        return True


    
        