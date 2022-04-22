class Solution(object):
    def minBitFlips(self, start, goal):
        binaryStart = bin(start)
        binaryGoal = bin(goal)

        if len(binaryStart) > len(binaryGoal):
          diff = len(binaryStart) - len(binaryGoal)
          zeros = "0" * diff
          binaryGoal = binaryGoal[:2] + zeros + binaryGoal[2:]
        elif len(binaryStart) < len(binaryGoal):
          diff = len(binaryGoal) - len(binaryStart)
          zeros = "0" * diff
          binaryStart = binaryStart[:2] + zeros + binaryStart[2:]

        count = 0
        for element in range(0, len(binaryGoal)):
            if binaryGoal[element] != binaryStart[element]:
              count = count + 1
        
        return count
        