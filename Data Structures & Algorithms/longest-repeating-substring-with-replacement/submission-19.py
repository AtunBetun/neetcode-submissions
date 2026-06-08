class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0

        for r in range(len(s)):
            count = list(Counter(s[l:r+1]).items())
            count.sort(reverse=True, key=lambda x: x[1])
            char_count = count[0]
            str_len = r-l+1
            replacements = str_len - char_count[1]
            print(f"{l=} {r=} {count=} {char_count=} {str_len=} {replacements=}")
            if replacements <= k:
                longest = max(longest, str_len)
            while replacements > k:
                print(f"TOO LONG: {l=} {r=} {count=} {char_count=} {str_len=} {replacements=}")
                l += 1
                count = list(Counter(s[l:r+1]).items())
                count.sort(reverse=True, key=lambda x: x[1])
                char_count = count[0]
                str_len = r-l+1
                replacements = str_len - char_count[1]
        return longest