class Node:
    
    def __init__(self):
        self.children = {}
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for i in word:
            if i not in cur.children:
                cur.children[i] = Node()
            cur = cur.children[i]
        
        cur.isword = True

    def search(self, word: str) -> bool:
        
        def dfs(c, i):
            
            for w in range(i, len(word)):
                if word[w] == ".":
                    for child in c.children.values():
                        if dfs(child, w + 1):
                            return True
                    return False
                else:
                    if word[w] not in c.children:
                        return False
                    c = c.children[word[w]]

            return c.isword
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)