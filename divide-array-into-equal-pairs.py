class Solution(object):
    def divideArray(self, nums):
        nums.sort()
        chunks = [nums[x:x+2] for x in range(0, len(nums), 2)]

        bool = True;
        for x in chunks:
          bool = x.count(x[0]) == len(x)
          if bool == False:
            break
        
        return bool