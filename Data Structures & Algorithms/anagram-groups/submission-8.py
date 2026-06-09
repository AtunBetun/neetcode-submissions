from collections import defaultdict
import json

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #
        def get_anagram_type(curr: str) -> str:
            count = Counter(curr)
            count = dict(sorted(count.items(), key=lambda item: item[0]))
            return json.dumps(count)
        
        # 1. master dict of "".join of a dicts value -> anagram list -> dict of []
        ans = defaultdict(list)
        # Algo
        for curr_str in strs:
            ana = get_anagram_type(curr_str)
            ans[ana].append(curr_str)
        return list(ans.values())
        

