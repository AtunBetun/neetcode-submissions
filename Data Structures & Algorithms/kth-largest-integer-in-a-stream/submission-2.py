import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for x in nums:
            heapq.heappush(self.h, -x) # max heap
        print(f"{self.h=}")

    def add(self, val: int) -> int:
        heapq.heappush(self.h, -val)

        a = []
        c = None
        for i in range(self.k):
            c = heapq.heappop(self.h)
            a.append(c)
        print(0)
        for x in a:
            heapq.heappush(self.h, x)
        return -c