class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking algorithm
        # order matters for the answer
        # answer can not contain duplicates

        # keep dictionary as key of the path so far
        ans = []
        def dp(i, path, used):
            if len(path) == len(nums): # new permutation base case
                ans.append(path[:]) # copy of the answer
                return

            for j in range(len(nums)): # left to right
                if not used[j]:
                    used[j] = True
                    path.append(nums[j])
                    dp(j+1, path, used)
                    path.pop()
                    used[j] = False

        dp(0, [], [False] * len(nums))
        print(f"{ans=}")
        return ans