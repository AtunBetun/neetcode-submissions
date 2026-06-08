import json
class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '\0'
        return '\0'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '\0':
            return []
        return s.split('\0')
