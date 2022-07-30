class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:        
        result = []
        nums.sort()

        for x in range(0,len(nums)):
            if target == nums[x]:
                result.append(x)
                
        return result