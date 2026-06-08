class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def dp(i, path):
            curr = sum(path) if path else 0
            print(f"{i=} {curr=} {path=}")
            if curr == target:
                self.ans.append(path.copy())
                return
            if curr > target or i >= len(nums):
                return

            # include nums[i]
            path.append(nums[i])
            dp(i, path)  # use again
            path.pop()
            # skip nums[i]
            dp(i + 1, path)

        dp(0, [])
        return self.ans
