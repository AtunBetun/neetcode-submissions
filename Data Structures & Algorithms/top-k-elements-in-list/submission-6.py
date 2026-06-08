class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        count = sorted(count.items(), key=lambda item: item[1], reverse=True)
        print(count)
        ans = []
        for x in range(0, k):
            ans.append(count[x][0])
        print(ans)
        return ans

