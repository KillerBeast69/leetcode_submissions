class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sortedarr = sorted(arr)
        final = []
        small = float("inf")
        for i in range (len(sortedarr) - 1):
            diff = sortedarr[i+1] - sortedarr[i]
            if diff < small:
                small = diff
        for j in range (len(sortedarr) - 1):
            if sortedarr[j+1] - sortedarr[j] == small:
                final.append([sortedarr[j], sortedarr[j+1]])
        return final
