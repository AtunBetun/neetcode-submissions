class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dp(i, path):
            if i == len(nums):
                ans.append(path[:])  # clone the list
                return

            # don't include nums[i]
            dp(i + 1, path)

            # include nums[i]
            path.append(nums[i])
            dp(i + 1, path)
            path.pop()  # backtrack

        dp(0, [])
        return ans


