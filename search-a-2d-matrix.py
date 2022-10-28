class Solution:
    def binarySearch(self, nums, low, high, target):
        if high >= low:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return self.binarySearch(nums, low, mid-1, target)
            else:
                return self.binarySearch(nums, mid + 1, high, target)
        else:
            return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = sum(matrix,[])
        return self.binarySearch(nums, 0, len(nums)-1, target)
        