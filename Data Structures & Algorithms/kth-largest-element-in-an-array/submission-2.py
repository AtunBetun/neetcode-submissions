import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for x in nums:
            heapq.heappush(h, -x)
        
        for i in range(0, k-1):
            heapq.heappop(h)    
        return -h[0]
