class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bt(r, c, seen):
            i = (r, c)
            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or i in seen
            ):
                return
            if grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"

            seen.add(i)
            bt(r-1, c, seen)
            bt(r+1, c, seen)
            bt(r, c-1, seen)
            bt(r, c+1, seen)
            return

        ans = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == "1":
                    ans += 1
                    bt(r, c, set())
        return ans