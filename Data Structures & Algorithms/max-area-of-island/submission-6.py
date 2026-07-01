class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        def bt(r, c, seen) -> int:
            i = (r, c)
            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or i in seen
            ):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = (
                1 +
                bt(r+1, c, seen) +
                bt(r-1, c, seen) +
                bt(r, c+1, seen) +
                bt(r, c-1, seen)
            )
            return area
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    ans = max(bt(r, c, set()), ans)
        return ans 