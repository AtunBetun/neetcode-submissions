class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_1 = Counter(s)
        c_2 = Counter(t)
        return c_1 == c_2