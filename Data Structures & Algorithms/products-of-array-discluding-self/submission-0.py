class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
    
        # Left pass: output[i] = product of all elements to the left of i
        left_product = 1
        for i in range(n):
            print(f"{i=} {left_product=}")
            output[i] = left_product
            left_product *= nums[i]
        print(f"{output=}")
    
        # Right pass: multiply output[i] with product of elements to the right of i
        right_product = 1
        for i in reversed(range(n)):
            print(f"{i=} {right_product=}")
            output[i] *= right_product
            right_product *= nums[i]
        return output

        