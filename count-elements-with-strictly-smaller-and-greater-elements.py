class Solution:
    def countElements(self, nums: List[int]) -> int:
        numsTemp = nums
        setNums = set(numsTemp)
        if len(setNums) == 2 or len(setNums) == 1 or len(nums) == 1:
            return 0

        nums.sort()
        lowest = nums[0]
        highest = nums[len(nums)-1]
        lowestCount = nums.count(lowest)
        highestCount = nums.count(highest)

        nums.sort(reverse=True)
        for x in range(0,lowestCount):
            nums.pop()

        nums.sort()
        for x in range(highestCount):
            nums.pop()

        return len(nums)