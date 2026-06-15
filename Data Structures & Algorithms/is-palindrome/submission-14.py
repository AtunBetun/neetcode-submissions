class Solution:
    def isPalindrome(self, s: str) -> bool:
        # collapse into the middle
        # either even or non even
        even = len(s) % 2 == 0 
        s = "".join(char for char in s if char.isalnum())
        l = 0
        r = len(s) - 1
        while l < r:
            print(f"{l=} {s[l]=} {r=} {s[r]=}")
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True