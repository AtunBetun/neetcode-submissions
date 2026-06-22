class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = []
        for i, x in enumerate(nums):
            new_nums.append((i, x))
        new_nums.sort(key=lambda x: x[1])
        print(f"{new_nums=}")
        l, r = 0, len(nums) - 1
        while l < r:
            curr = new_nums[l][1] + new_nums[r][1]
            print(f"{l=} {r=} {curr=} {nums[l]=} {nums[r]=}")
            if curr == target:
                ans = [new_nums[l][0], new_nums[r][0]]
                ans.sort()
                return ans
            elif curr > target:
                r -= 1
            elif curr < target:
                l += 1
        print(new_nums)
        return []
        