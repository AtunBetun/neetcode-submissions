class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_sell = 0
        min_price = float('inf')
        for x in prices:
            min_price = min(min_price, x)
            sell = x - min_price
            max_sell = max(sell, max_sell)
        return max_sell
