class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while(num>0):
            sum = num % 10
            if temp % sum == 0:
                print(sum)
                count = count + 1
            num = num//10
        return count 


