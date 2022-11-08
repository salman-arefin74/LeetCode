class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        minSteps = 0

        while target > 1:
            if maxDoubles == 0:
                minSteps += target - 1
                return minSteps
            if target % 2 == 0 and target > 2 and maxDoubles > 0:
                target = target // 2
                minSteps += 1
                maxDoubles -= 1
            else:
                target -= 1
                minSteps += 1
        
        return minSteps

