class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = 0
        for i in range(0, len(words)):
            if s.startswith(words[i]):
                counter = counter + 1
        return counter
