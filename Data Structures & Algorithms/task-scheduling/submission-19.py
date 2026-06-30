from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = dict(Counter(tasks))
        h = []
        cool = deque([])
        cycle = 0
        for k, v in c.items():
            heapq.heappush(h, (-v, k))
        
        while h or cool: 
            print(f"{h=} {cool=} {cycle=}")
            while cool and cool[0][0] <= cycle:
                t = cool.popleft()
                t = (t[1], t[2])
                heapq.heappush(h, t)

            if h:
                t = heapq.heappop(h)
                t = (t[0]+1, t[1])
                print(f"{t=}")
                if t[0] < 0:
                    new_t = (cycle + n + 1, t[0], t[1])
                    print(f"{new_t=}")
                    cool.append(new_t)
            
            cycle += 1

        return cycle