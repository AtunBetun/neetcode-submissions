class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # backtrack algorithm
        ans = []
        def bt(i, path):
            ans.append(path[:]) # current path
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                bt(j+1, path)
                path.pop()
        bt(0, [])
        return ans