class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        divisors = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)

        
        total = 0

        for k in divisors:
            possible = True

            blocks = []

            for i in range(0, n, k):
                block = nums[i : i + k]

                sorted_block = sorted(block)

                blocks.append((block, sorted_block))

            for block, sorted_block in blocks:
                doubled = block + block
                found = False

                drops = 0

                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        drops += 1
                
                if drops > 1:
                    possible = False
                    break
                
                if sorted(block) != sorted_block:
                    pass

            
            if not possible:
                continue

            
            for i in range(len(blocks) - 1):
                max_current = max(blocks[i][1])
                min_next = min(blocks[i + 1][1])

                if blocks[i][1][-1] > blocks[i + 1][1][0]:
                    possible = False
                    break

            if possible:
                total += k
            
        return total