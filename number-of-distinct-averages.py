class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgList = []
        nums.sort()

        while nums:
            maxNumber = nums.pop(0)
            minNumber = nums.pop(-1)
            avgList.append((maxNumber + minNumber) / 2)

        avgList = set(avgList)

        return len(avgList)