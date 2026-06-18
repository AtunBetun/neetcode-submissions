class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num, t = numbers, target
        l, r = 0, len(numbers) - 1
        while l < r:
            curr = num[l] + num[r]
            if curr == t:
                return [l+1, r+1]
            elif curr > t:
                r -= 1
            else:
                l +=1 
