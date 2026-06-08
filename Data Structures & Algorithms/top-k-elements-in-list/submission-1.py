class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(Counter(nums).items())
        count.sort(key=lambda x: x[1], reverse=True)
        ans = []
        for x in range(0, k):
            ans.append(count[x][0])
        return ans
        