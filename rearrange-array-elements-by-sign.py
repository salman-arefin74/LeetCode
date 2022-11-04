class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        res = [0] * len(nums)

        for item in nums:
            if item > 0:
                res[i] = item
                i += 2
            elif item < 0:
                res[j] = item
                j += 2
                
        return res
