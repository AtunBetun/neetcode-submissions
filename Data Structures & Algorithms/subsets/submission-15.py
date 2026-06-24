from copy import deepcopy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(i, path):
            if i >= len(nums):
                ans.append(deepcopy(path))
                return

            # use
            path.append(nums[i])
            bt(i+1, path)

            # dont use
            path.pop()
            bt(i+1, path)
        bt(0, [])
        return ans