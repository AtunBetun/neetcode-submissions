from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
            if d[x] == 2:
                return x