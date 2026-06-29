class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def bt(i, path):
            a = tuple(path)
            if i >= len(nums) or len(path) == len(nums):
                if a not in ans:
                    ans.add(a)
                return
            
            for j in range(0, len(nums)):
                if nums[j] not in path:
                    path.append(nums[j])
                    bt(i + 1, path)
                    path.pop()
        bt(0, [])
        print(f"{ans=}")
        ans = [list(x) for x in ans]
        print(f"{ans=}")
        return ans