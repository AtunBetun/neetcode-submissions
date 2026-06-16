class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # keeps track of the latest min element

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif self.minStack and val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if self.minStack and curr == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
