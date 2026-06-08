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

        while l < r:
            m = (l+r) // 2
            if can_eat(m): # all to the right I don't care
                r = m # keep m as possible answer
            else:
                l = m + 1
        return l
