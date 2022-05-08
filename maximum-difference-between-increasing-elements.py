class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] < nums[y] and (nums[y] - nums[x]) > maxDiff:
                    maxDiff = nums[y] - nums[x]
                    
        return maxDiff