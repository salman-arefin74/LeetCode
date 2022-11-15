class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val1 in enumerate(nums):
            if i > 0 and val1 == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                if val1 + nums[j] + nums[k] > 0:
                    k -= 1
                elif val1 + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([val1, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res