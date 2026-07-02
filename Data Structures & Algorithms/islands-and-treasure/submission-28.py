from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        que = deque([])
        def neighbors(r, c):
            return [
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ]

        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 0:
                    for x in neighbors(r, c):
                        que.append((x[0], x[1], 0))


        while que:
            print(f"{que=}")
            r, c, count = que.popleft()
            print(f"{r=} {c=} {count=}")
            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or grid[r][c] != 2147483647
            ):
                continue
            grid[r][c] = count + 1
            for x in neighbors(r, c):
                print(f"{r=} {c=} {x=}")
                que.append((x[0], x[1], count+1))