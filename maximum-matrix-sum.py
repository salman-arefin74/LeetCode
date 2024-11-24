class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = 0
        negative_count = 0
        minimum_negative = float("inf")

        for row in matrix:
            for value in row:
                result += abs(value)
                minimum_negative = min(minimum_negative, abs(value))
                if value < 0:
                    negative_count += 1

        if negative_count & 1:
            result = result - (2 * minimum_negative)
        
        return result
