class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def dp(i, state):
            curr = sum(state) if state else 0
            print(f"{i=} {curr=} {state=}")
            if curr == target:
                self.ans.append(state.copy())
                return
            if curr > target or i >= len(nums):
                return

            # include nums[i]
            state.append(nums[i])
            dp(i, state)  # use again
            state.pop()

            # skip nums[i]
            dp(i + 1, state)

        dp(0, [])
        return self.ans
