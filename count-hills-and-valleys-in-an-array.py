class Solution(object):
    def find_left_neighbor(self, index, list):
        leftNeighbor = 0
        for x in range(index-1, -1, -1):
            if list[index] != list[x]:
                leftNeighbor = list[x]
                break
            return leftNeighbor

    def find_right_neighbor(self, index, list):
        rightNeighbor = 0
        for x in range(index + 1, len(list)):
            if list[index] != list[x]:
                rightNeighbor = list[x]
                break
        return rightNeighbor


    def countHillValley(self, nums):
        lastState = ""
        count = 0
        left = 0
        right = 0
        for x in range(1, len(nums)-1):
            if(nums[x] == nums[x-1]):
                left = self.find_left_neighbor(x, nums)
            else:
                left = nums[x-1]

            if(nums[x] == nums[x+1]):
                right = self.find_right_neighbor(x, nums)
            else:
                right = nums[x+1]

            if nums[x] > left and nums[x] > right and lastState != "hill" and left != 0 and right != 0:
                count = count + 1
                lastState = "hill"
            elif nums[x] < left and nums[x] < right and lastState != "valley" and left != 0 and right != 0:
                count = count + 1
                lastState = "valley"
        
        return count