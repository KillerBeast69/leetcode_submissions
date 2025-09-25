class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, w, i):
        cur = self.root
        for ch in w:
            c = ord(ch) - ord('a')
            if not cur.children[c]:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.index = i

    def search(self, w):
        cur = self.root
        for ch in w:
            c = ord(ch) - ord('a')
            if not cur.children[c]:
                return -1
            cur = cur.children[c]
        return cur.index

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.CHAR = '{'
        for i, w in enumerate(words):
            w_len = len(w)
            for j in range(w_len):
                suffix = w[j:]
                for k in range(w_len + 1):
                    prefix = w[:k]
                    self.trie.addWord(suffix + self.CHAR + prefix, i)

    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(suff + self.CHAR + pref)
