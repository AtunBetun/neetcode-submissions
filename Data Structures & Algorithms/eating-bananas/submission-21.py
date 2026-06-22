import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        def can_eat(k: int) -> bool:
            hours = 0
            for x in piles:
                hours += math.ceil(x / k)
            return hours <= h
        r = sum(piles)
        l = 1
        while l < r:
            m = (l+r) // 2
            print(f"{l=} {m=} {r=}")
            if not can_eat(m):
                l = m + 1
            else:
                r = m
        print(f"{piles=}")
        return l