class PrefixTree:
    END = "#"

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        node = self.d
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and self.END in node

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.d
        for c in s:
            if c not in node:
                return None
            node = node[c]
        return node