class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #not sure how but we have to check if a side of the rectangle intersects the side of other rectangle, if so then we return true. In a rectangle, we check if line connecting points x1 and x2 lie between y1 and y2 of the other rectangle, if so then we check if either of line connecting x2 and x2 y2 or the line x1 y1 and y2 lie between the points x1 and x2. 

        ax1 = rec1[0]
        ax2 = rec1[2]
        ay1 = rec1[1]
        ay2 = rec1[3]

        bx1 = rec2[0]
        bx2 = rec2[2]
        by1 = rec2[1]
        by2 = rec2[3]

        if ax2 <= bx1 or ay1 >= by2 or ax1 >= bx2 or ay2 <= by1:
            return False
        return True
        