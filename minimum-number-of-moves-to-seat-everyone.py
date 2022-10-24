class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()

        moves = 0
        for i in range(len(seats)):
          moves = moves + (abs(students[i] - seats[i]))
        
        return moves