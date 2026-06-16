class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in range(0, len(s)):
            curr = s[i]
            if stack and curr in d and d[curr] == stack[-1]:
                stack.pop()
            else:
                stack.append(curr)

        return stack == []
        