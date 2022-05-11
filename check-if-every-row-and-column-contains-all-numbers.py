class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        valid = True
        rowCheck = matrix[0]
        for x in matrix:
            if set(rowCheck) != set(x) or len(set(rowCheck)) != len(matrix):
                valid = False
                break
        if valid == False:
            return valid

        colCheck = [val[0] for val in matrix]
        for x in range(1, len(matrix)):
            newCol = [val[x] for val in matrix]
            if set(colCheck) != set(newCol) or len(set(colCheck)) != len(matrix):
                valid = False
                break

        return valid