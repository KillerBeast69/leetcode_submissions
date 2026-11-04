class Node:

    def __init__(self):
        self.children = {}
        self.isword = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
            else:
                cur.children[i] = Node()
                cur = cur.children[i]
        
        cur.isword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
                continue
            return False
        
        return cur.isword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)