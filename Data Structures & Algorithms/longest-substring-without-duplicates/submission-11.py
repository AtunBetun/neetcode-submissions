class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        longest = 0
        for r in range(0, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1 
            seen.add(s[r])
            curr_len = r - l + 1
            longest = max(curr_len, longest)
        return longest