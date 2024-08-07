class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        a = 0
        b = 0
        merge = []
        word = 1
        while (a<l1 and b<l2):
            if (word == 1):
                merge.append(word1[a])
                a = a+1
                word = 2
            else:
                merge.append(word2[b])
                b = b+1
                word = 1
        while (a<l1):
            merge.append(word1[a])
            a = a+1
        while (b<l2):
            merge.append(word2[b])
            b = b+1
        return ''.join(merge)
            
