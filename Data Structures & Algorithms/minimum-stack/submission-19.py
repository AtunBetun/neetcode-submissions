class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal: int | None = None
        

    def push(self, val: int) -> None:
        print(f"push: {val=}")
        self.stack.append(val)
        if self.minVal is None or val <= self.minVal:
            self.minVal = val
            self.minStack.append(val)
        print(f"{self.stack=} {self.minVal=} {self.minStack=}")

    def pop(self) -> None:
        print(f"pop")
        if self.stack == []:
            return None

        c = self.stack[-1]
        m = self.minStack[-1]
        print(f"{c=} {m=}")

        if len(self.stack) >= 2:
            if c == m:
                self.minStack.pop()
                self.minVal = self.minStack[-1]
        else:
            self.minStack.pop()
            self.minVal = None

        
        self.stack.pop()
        print(f"{self.stack=} {self.minVal=} {self.minStack=}")
        
    def top(self) -> int:
        print(f"top")
        print(f"{self.stack=} {self.minVal=} {self.minStack=}")
        return self.stack[-1]

    def getMin(self) -> int:
        print(f"getMin")
        print(f"{self.stack=} {self.minVal=} {self.minStack=}")
        return self.minVal
        
