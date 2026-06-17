class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = float("-inf")

        # i = 2
        # j = 5
        def mono(i: int, numbers, d):
            print(f"mono: {i=} {numbers=}")
            s = []
            nonlocal ans
            for j in numbers:
                if not s or heights[j] <= s[-1]:
                    s.append(heights[j])
    

                # see
                if d == "r":
                    area = (j - i + 1) * s[-1]
                else:
                    area = (i - j + 1) * s[-1]
                ans = max(ans, area)

        for i in range(0, len(heights)):
            print(f"box: {i=} {ans=}")
            mono(i, range(i, len(heights)), "r")
            mono(i, range(i, -1, -1), "l")
        
        return ans