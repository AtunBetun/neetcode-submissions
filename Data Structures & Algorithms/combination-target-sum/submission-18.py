from copy import deepcopy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        def bt(i, path):
            nonlocal ans
            # print(f"{i=} {path=}")
            if i >= len(nums) or sum(path) >= target:
                if sum(path) == target:
                    #print(f"found: {i=} {path=}")
                    c = deepcopy(path)
                    c.sort()
                    c = tuple(c)
                    if c not in ans:
                        ans.add(c)
                # flush
                return

            bt(i + 1, path) # skip

            path.append(nums[i]) # use and reuse
            bt(i, path)
            path.pop()

            path.append(nums[i]) # use and next element
            bt(i+1, path)
            path.pop()
            return
        bt(0, [])
        a = []
        for x in ans:
            a.append(list(x))
        return a