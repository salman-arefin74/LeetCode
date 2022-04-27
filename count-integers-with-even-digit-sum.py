class Solution:
    def countEven(self, num: int) -> int:
        sumOfDigits = 0
        isEven = False
        count = 0
        for x in range(1,num+1):
            if x < 10 and x%2 == 0:
                count = count + 1
            else:
                digits = [int(digit) for digit in str(x)]
                sumOfDigits = sum(digits)
                if sumOfDigits%2 == 0:
                    count = count + 1
                    
        return count