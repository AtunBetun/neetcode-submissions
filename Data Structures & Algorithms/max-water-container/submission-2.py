class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        l, r = 0, len(h) - 1
        ans = float("-inf")
        while l < r:
            area = min(h[l], h[r]) * (r - l)
            ans = max(ans, area)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return ans