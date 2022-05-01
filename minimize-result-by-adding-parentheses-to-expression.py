class Solution:
    def minimizeResult(self, expression: str) -> str:
        splitExpr = expression.split('+')
        leftExpr = []
        rightExpr = []
        possibleExpr = []

        for x in range(len(splitExpr[0])):
            leftExpr.append(self.insert_char(splitExpr[0], x, '('))

        for x in range(1, len(splitExpr[1])+1):
            rightExpr.append(self.insert_char(splitExpr[1], x, ')'))

        for x in range(len(leftExpr)):
            for y in range(len(rightExpr)):
                possibleExpr.append(leftExpr[x] + '+' + rightExpr[y])

        value = self.valueOfExpression(possibleExpr[0])
        tempValue = value
        result = possibleExpr[0]
        for x in range(1, len(possibleExpr)):
            tempValue = self.valueOfExpression(possibleExpr[x])
            if tempValue < value:
                value = tempValue
                result = possibleExpr[x]
        
        return result
    

    def valueOfExpression(self, expression: str) -> int:
        if expression[0] != '(':
            expression = expression.replace("(", "*(")
        if expression[len(expression) - 1] != ')':
            expression = expression.replace(")", ")*")

        return eval(expression)

    def insert_char(self, string: str, index: int, char: str) -> str:
        return string[:index] + char + string[index:]
