class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            print(f"{i=} {n=}")
            miss = target - n
            if miss in seen:
                return[seen[miss], i]

            seen[n] = i
        return []