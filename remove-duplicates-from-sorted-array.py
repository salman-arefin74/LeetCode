class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i + 1
        count = 1
        for k in range(len(nums) - 1):
            if nums[i] == nums[j]:
                nums[j] = 101
                j += 1
            else:
                i = j
                j += 1
                count += 1

        
        nums.sort()
        return count