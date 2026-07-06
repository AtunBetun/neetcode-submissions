from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        batch = []
        seen = set()
        t = 0
        total = 0
        curr = 0
        def neighbors(r, c):
            return [
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1)
            ]
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    total += 1
                if grid[r][c] == 2:
                    for x in neighbors(r, c):
                        batch.append((x[0], x[1]))
                        seen.add(x)
        que = deque([batch])
        while que:
            print(f"{que=}")
            b = que.popleft()
            t += 1
            print(f"{que=} {b=} {t=}")
            # process
            rotted = []
            for x in b:
                r, c = x[0], x[1]
                if (
                    r < 0
                    or r >= len(grid)
                    or c < 0
                    or c >= len(grid[0])
                    or grid[r][c] != 1
                ):
                    continue
                grid[r][c] = 2
                rotted.append((r, c))
                curr += 1
            batch = []
            print(f"    rotted: {rotted=}")
            for x in rotted:
                r, c = x[0], x[1]
                for y in neighbors(r, c):
                    if y not in seen:
                        seen.add((r, c))
                        batch.append((y[0], y[1]))
            if batch:
                que.append(batch)
        if curr == total:
            return t-1
        else:
            return -1