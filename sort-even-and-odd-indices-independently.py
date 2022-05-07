class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for x in range(len(nums)):
            if x%2 == 0:
                even.append(nums[x])
            else:
                odd.append(nums[x])

        even.sort()
        odd.sort(reverse=True)

        evenIndex = 0
        oddIndex = 0
        newNums = []
        for x in range(len(nums)):
            if x%2 == 0:
                newNums.insert(x, even[evenIndex])
                evenIndex = evenIndex + 1
            else:
                newNums.insert(x, odd[oddIndex])
                oddIndex = oddIndex + 1

        return newNums