class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle = 0
        square = 0
        for i in students:
            if i == 0:
                circle += 1
            else:
                square += 1
        for j in sandwiches:
            if j == 0:
                circle -= 1
                if circle < 0:
                    return circle + square + 1
            else:
                square -= 1
                if square < 0:
                    return circle + square + 1 
        return circle + square
