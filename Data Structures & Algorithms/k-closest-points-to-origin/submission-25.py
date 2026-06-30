import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        #print(f"{points=}")
        for i in range(0, len(points)):
            d = points[i][0]**2 + points[i][1]**2
            # print(f"{i=} {d=}")
            s = (math.sqrt(d), points[i])
            #print(f"{x=} {s=}")
            heapq.heappush(h, s)

        print(f"pre: {h=}")
        ans = []
        for i in range(k):
            # print(f"loop: {h=}")
            ans.append(heapq.heappop(h)[1])
        
        return ans