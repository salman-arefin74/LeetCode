class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        digits.sort()

        firstArr = str(digits[0]) + str(digits[2])
        secondArr = str(digits[1]) + str(digits[3])

        sum = int(firstArr) + int(secondArr)
        
        return sum