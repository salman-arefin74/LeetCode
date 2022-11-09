class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        def checkBallStatus(row,col) -> int:
            if row == rows:
                return col
            newCol = col + grid[row][col]

            if newCol == -1 or newCol == cols or grid[row][col] != grid[row][newCol]:
                return -1
            else:
                return checkBallStatus(row+1, newCol)

        answer = []
        for i in range(cols):
            answer.append(checkBallStatus(0,i))
        return answer
