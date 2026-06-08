class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [5,6,7,8,1,2,3,4]
        # if nums[m] < nums[r] # sorted => regular binary search
        # elif nums[m] > nums[r] # rotated => reverse binary search
        # nums=[3,4,5,6,1,2]
        # target=1
        #       l   m     r
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            print(f"{left=} {mid=} {right=}")
            if nums[mid] == target:
                return mid # index

            if nums[mid] < nums[right]: # right side sorted
                if target > nums[mid] and target <= nums[right]: # is right
                    left = mid + 1
                else:
                    right = mid - 1
            else: # left side is sorted
                if target < nums[mid] and target >= nums[left]: # is left
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
            
            

        