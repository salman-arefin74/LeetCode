class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newNums = []
        counterx = 0
        countery = n

        for i in range(len(nums)):
          if i % 2 == 0:
            newNums.append(nums[counterx])
            counterx += 1
          else:
            newNums.append(nums[countery])
            countery += 1
            
        return newNums