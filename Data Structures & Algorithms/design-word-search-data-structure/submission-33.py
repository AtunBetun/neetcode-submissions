class WordDictionary:
    def __init__(self):
        self.d = {}
        self.END = "#"

    def addWord(self, word: str) -> None:
        self._insert(word)

    def search(self, word: str) -> bool:
        node = self.d
        return self._dp(0, node, word)

    # i: curr index
    # node: last node
    # word: word we are searching
    def _dp(self, i: int, node: dict, word: str) -> bool:
        if i >= len(word): # reached end
            return self.END in node

        if word[i] != ".":
            if word[i] not in node:
                return False
            return self._dp(i+1, node[word[i]], word)
        
        for k in node:
            if k != self.END:
                if self._dp(i+1, node[k], word):
                    return True
        return False
        

    def _insert(self, word: str) -> None:
        node = self.d
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.END] = True
