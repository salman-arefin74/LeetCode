class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        newNums = []
        for num in nums:
            strDigit = ""
            for digit in str(num):
                integer = int(digit)
                strDigit += str(mapping[integer])
            newNums.append([num, int(strDigit)])

        newNums.sort(key=lambda item: item[1])

        result = []
        for i in newNums:
            result.append(i[0])  
    
        return result