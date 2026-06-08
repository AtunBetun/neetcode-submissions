class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        a = list(set(nums))
        a.sort()

        l = 0
        c = 0
        for i in range(0, len(a)):

            if i == len(a) - 1:
                break

            if a[i+1] == a[i] + 1:
                c += 1
                l = max(c, l)
            else:
                c = 0

        return l + 1

        