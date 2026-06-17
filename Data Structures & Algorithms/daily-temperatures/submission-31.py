class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, x in enumerate(temperatures):
            # found next higher up
            while stack and x > stack[-1][1]:
                last_min = stack.pop()
                ans[last_min[0]] = i - last_min[0]
            stack.append((i, x))
        return ans