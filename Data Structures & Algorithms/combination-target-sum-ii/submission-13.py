class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = candidates
        nums.sort()

        # keep a global ans
        # use backtracking
        # if found, then append to ans
        def dp(start, path):
            curr = sum(path)
            if curr == target:
                ans.append(path[:]) # copy of arr
            if curr > target:
                return
            for i in range(start, len(nums)):
                if i > start and candidates[i] == candidates[i - 1]:  # skip duplicates
                    continue
                path.append(nums[i])
                dp(i + 1, path)
                path.pop()
    
        dp(0, [])
        return ans

        

        




        