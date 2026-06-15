from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            print(r)

        rows = defaultdict(set)
        column = defaultdict(set)
        box = defaultdict(set)
        for i in range(0, 9):
            rows[i] = set()
            column[i] = set()
            box[i] = set()

        def get_box(r: int, c: int) -> int:
            box_num = 0

            # rows
            if r >= 3 and r <= 5:
                box_num += 3
            if r >= 6:
                box_num += 6

            # columns
            if c >= 3 and c <= 5:
                box_num += 1
            if c >= 6:
                box_num += 2
            return box_num

        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                curr = board[r][c]
                if curr == ".":
                    continue
                curr = int(curr)

                if curr < 1 or curr > 9:
                    print("OUT OF BOUNDS")
                    return False

                if curr in rows[r]:
                    print("EXISTING ROW")
                    return False
                rows[r].add(curr)
                if curr in column[c]:
                    print("EXISTING COLUMN")
                    return False
                column[c].add(curr)

                box_num = get_box(r, c)
                print(f"{box_num=}")
                if curr in box[box_num]:
                    print("EXISTING BOX")
                    return False
                box[box_num].add(curr)

        return True
