class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # I need to find the nearest palindrome
        def get_pal(n):
            s = str(n)
            l = len(s)
            d = int(s[0])
            hashset = set()
            prefix = s[:(l + 1) // 2]

            def make_pal(pre):
                if l % 2 == 0:
                    return pre + pre[::-1]
                else:
                    return pre + pre[:-1][::-1]

            p = int(prefix)

            hashset.add(int(make_pal(str(p - 1))))
            hashset.add(int(make_pal(str(p))))
            hashset.add(int(make_pal(str(p + 1))))

            # biggest and smallest digit with a digit difference

            if n % 2 == 0:
                hashset.add(int("2" + ("0" * (l - 1)) + "2"))
                if l > 2:
                    hashset.add(int("8" + ("9" * (l - 3)) + "8"))
                elif l == 2:
                    hashset.add(8)
            else:
                if l > 1:                    
                    hashset.add(int("9" * (l - 1)))
                hashset.add(int(("1" + ("0" * (l - 1)) + "1")))

            if l > 1:
                if d > 1:
                    hashset.add(int(str(d - 1) + ("9" * (l - 2)) + str(d - 1)))

                if d < 9:
                    hashset.add(int(str(d + 1) + ("0" * (l - 2)) + str(d + 1)))

            return hashset
            
        cost = 0
        for n in nums:
            even = False
            if n % 2 == 0:
                even = True
            s = str(n)
            if s == s[::-1]:
                continue
            candidates = get_pal(n)
            best_diff = float('inf')
            best = 0
            for c in candidates:
                parity = False
                if c % 2 == 0:
                    parity = True
                if c <= 0 or (parity != even):
                    continue

                if abs(n - c) < best_diff:
                    best_diff = abs(n - c)
                    best = c
            
            cost += abs(n - best) // 2

        return cost

            # if the number is single digit or a palindrome we continue
            # if not then, we check the first number?
            # we have to reach to a point where the parity of first number and last number matches
            # if the parity of last number does not match with the first
            # we have to reach to a point where the parirt matches
            # also we have to find a way with minimun number of operations
            # first phase is finding the closest palindrome

            # to find the nearest palindrome, I have to get the first half of the given number
            # then mirror it and calculate how many jumps it take to get to that number
            # but what if the next closest palindrome is not by mirroring the first half??
            # if mirroring the left half does not give the same parity, 
            # then we know we cannot reach to that element
            # now sure what to do then
            # if we were mirroring from left? maybe shift that pointer to right and mirror again
            # how do I generate multiple palindrome numbers??
            # when should I consider numbers with more or less 1 digit

            

            # this is getting complicated
            # how to calculate boundry palindromes??
