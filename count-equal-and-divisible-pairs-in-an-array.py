class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0

        for x in range(len(nums)):
            for y in range(len(nums)):
                if x < y and nums[x] == nums[y] and (x*y)%k == 0:
                    count = count + 1
        
        return count

