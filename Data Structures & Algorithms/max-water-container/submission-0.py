class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        l, r = 0, len(h) - 1
        ans = -1
        while l < r:
            curr = min(h[l], h[r]) * (r - l)
            ans = max(ans, curr)
            if h[l] < h[r]:
                l +=1
            else:
                r -= 1
        return ans
