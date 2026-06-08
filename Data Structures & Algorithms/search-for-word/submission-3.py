class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # backtrack algorithm
        # global variable ans
        # recurse on up, down, left, right
        # check if found

        rows = len(board)
        cols = len(board[0])
        def dp(r, c, path, i):
            k = (r,c)
            if i == len(word): # we just found the word
                return True
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or k in path # already seen
            ): # invalid cases
                return False
            if (
                board[r][c] != word[i]
            ): # invalid cases
                return False

            
            path.append(k)
            i += 1
            res = (
                dp(r - 1, c, path, i) or # up
                dp(r + 1, c, path, i) or # down
                dp(r, c - 1, path, i) or # left
                dp(r, c + 1, path, i)    # right
            )
            path.pop()
            return res
            
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == word[0]:
                    ans = dp(row, col, [], 0)
                    if ans:
                        return True
        return False