import heapq
class MedianFinder:

    def __init__(self):
        self.h = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h, num)

    def findMedian(self) -> float:
        print(f"{self.h=}")
        # edge cases
        if len(self.h) == 1:
            return float(self.h[0])

        even = len(self.h) % 2 == 0
        temps = []
        for i in range(0, int(len(self.h) / 2)):
            temps.append(heapq.heappop(self.h))
        ans = None
        print(f"{temps=} {self.h=}")
        if even:
            ans = (temps[-1] + self.h[0]) / 2
        else:
            ans = float(self.h[0])
        for x in temps:
            heapq.heappush(self.h, x)
        return ans
