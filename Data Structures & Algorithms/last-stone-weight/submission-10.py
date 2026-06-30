import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for x in stones:
            heapq.heappush(h, -x)

        while h:
            print(f"loop: {h=}")
            if len(h) < 2:
                print(f"{h=}")
                return (h[0])*-1
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            print(f"{x=} {y=}")

            if x == y:
                continue
            if abs(x - y) > 0:
                y = abs(x-y)
                heapq.heappush(h, -y)
        return 0    