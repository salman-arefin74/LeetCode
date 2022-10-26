class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = False
        numsSet = set(nums)
        if len(nums) > len(numsSet):
          result = True
        
        return result