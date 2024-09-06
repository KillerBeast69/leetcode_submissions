class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1 = coordinate1[1]
        if int(x1) % 2 == 0:
            sum1 = 1
        else:
            sum1 = 0
        y1 = coordinate1[0]
        if ord(y1) % 2 == 0:
            sum2 = 1
        else:
            sum2 = 0
        result1 = (sum1 + sum2) % 2
        x2 = coordinate2[1]
        if int(x2) % 2 == 0:
            sum3 = 1
        else:
            sum3 = 0
        y2 = coordinate2[0]
        if ord(y2) % 2 == 0:
            sum4 = 1
        else:
            sum4 = 0
        result2 = (sum3 + sum4) % 2

        return result1 == result2
        
