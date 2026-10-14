class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = {}
        window = {}

        for letter in t:
            if letter not in tcount:
                tcount[letter] = 0
            
            tcount[letter] += 1
        
        l = 0
        res, reslen = [-1, -1], float("inf")
        have, need = 0, len(tcount)
        for r in range(len(s)):
            current = s[r]
            
            if current not in window:
                    window[current] = 0
            window[current] += 1

            if current in tcount and window[current] == tcount[current]:
                    have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                
                l += 1
        l, r = res

        return s[l : r + 1] if reslen != float("inf") else ""
