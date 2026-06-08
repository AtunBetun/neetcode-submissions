class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            print(f"{l=} {r}")
            if l == r:
                return nums[l]

            m = (l+r) // 2
            if nums[m] < nums[r]: # is on left, including
                r = m
            else:
                l = m + 1

        return nums[l]

        # [6,1,2,3,4,5]
        #  l   m     r
        # => l > m, m < r ==> go left
        #  l m r
        # => l > m, m < r 
        #  l r
        #  m
        # => l

        # [5,6,1,2,3,4]
        #  l   m     r
        #   => l > m, m < r ==> go left

        # [1,2,3,4,5]
        #  l   m     r
        #   => l < m < r ==> return nums[l]


        # [3,4,5,6,1,2]
        #  l   m     r
        #   => l > m, m < r ==> go left

