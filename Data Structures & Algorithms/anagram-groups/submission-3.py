class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for x in strs:
            count = [0] * 26
            for s in x:
                count[ord(s) - ord('a')] += 1
            print(f"{x=} {count=}")
            d[tuple(count)].append(x)
        print(d)
        ans = list(x[1] for x in d.items())
        print(ans)
        return ans



        