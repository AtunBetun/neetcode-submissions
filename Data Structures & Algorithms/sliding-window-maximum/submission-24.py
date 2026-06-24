from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        l = 0
        ans = []

        for r in range(len(nums)):
            # monotonic decreasing deque -> store indices to handle window removal
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # remove indices that are out of the current window
            if l > q[0]:
                q.popleft()

            if r >= k - 1:
                ans.append(nums[q[0]])
                l += 1
        return ans