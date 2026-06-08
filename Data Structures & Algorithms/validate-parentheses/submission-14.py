class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        for i in range(0, len(s)):
            print(f"{s=} {a=} {i=} {s[i]=}")
            if s[i] in ['(', '{', '[']:
                print(f"found beginning")
                a.append(s[i])
                continue

            if a == []:
                return False

            c = a[-1]
            print(f"{s=} {a=} {i=} {s[i]=} {c=}")
            if c == '(' and s[i] != ')':
                return False
            if c == '{' and s[i] != '}':
                return False
            if c == '[' and s[i] != ']':
                return False
            a.pop()
        if a == []:
            return True
        return False