class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        ans = []
        # first pointer
        print(nums)
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr = [nums[i], nums[l], nums[r]]
                curr.sort()
                curr_s = tuple(curr)

                if curr_s not in seen and sum(curr) == 0: # found ans
                    ans.append(curr)
                    seen.add(curr_s)

                if sum(curr) > 0:
                    r -= 1
                else:
                    l += 1
        return ans

