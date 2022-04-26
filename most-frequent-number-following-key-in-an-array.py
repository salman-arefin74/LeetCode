class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        potentialTargets = []

        for x in range(len(nums)-1):
            if(nums[x] == key):
                potentialTargets.append(nums[x+1])

    
        target = max(set(potentialTargets), key=potentialTargets.count)
        
        return target