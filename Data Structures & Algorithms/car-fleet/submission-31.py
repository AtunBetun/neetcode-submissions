class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pattern -> reactive stack
        arr = []
        stack = []
        for i in range(0, len(position)):
            t = (target - position[i]) / speed[i]
            arr.append((position[i], speed[i], t))
        arr.sort(key=lambda x: x[0], reverse=True)

        for x in arr:
            if stack and x[2] <= stack[-1]: # faster or equal -> gets joined to fleet
                continue
            else: # slower -> new fleet
                stack.append(x[2]) # append time

        
        return len(stack) # of fleets