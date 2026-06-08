class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        print(f"{piles=} {h=}")
        l = 1 # min
        r = max(piles) # max

        def can_eat(k) -> bool:
            hours = 0
            for x in piles:
                hours += math.ceil(x/k)
            if hours <= h:
                return True
            return False

        while l <= r: # binary search
            m = (l+r) // 2
            print(f"{l=} {r=} {m=}")
            if can_eat(m):
                r = m - 1
            else:
                l = m + 1
        return l
