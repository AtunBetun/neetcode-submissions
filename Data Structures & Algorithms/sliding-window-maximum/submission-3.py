from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        l = 0
        ans = []
        # monotonic decreasing deque

        def get_max(curr_q: deque) -> int:
            a = float("-inf")
            for x in curr_q:
                a = max(a, x)
            return a

        for r in range(len(nums)):
            q.append(nums[r])
            while len(q) >= k:
                ans.append(get_max(q))
                q.popleft()
        return ans