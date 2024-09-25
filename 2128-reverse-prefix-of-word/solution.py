class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        txt = word
        if ch in word:
            index = word.index(ch)
            txt = word[index: : -1] + word[index + 1: len(word): 1]
        return txt




