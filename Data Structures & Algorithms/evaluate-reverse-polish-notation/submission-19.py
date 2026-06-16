class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sym = ["+", "-", "*", "/"]
        s = []

        def result(op: str, first: int, second: int) -> int:
            res = None
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return int(first * second)
            else:
                return int(first / second)
            

        for x in tokens:
            s.append(x)
            if x in sym: # found symbol
                op = s.pop() # pop the symbol
                second = int(s.pop())
                first = int(s.pop())
                res = result(op, first, second)
                s.append(res)
        return int(s[-1])