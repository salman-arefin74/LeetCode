class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for letter in s:
            if len(stack) == 0 and (letter == ')' or letter == '}' or letter == ']'):
                return False
            elif letter == ')' and stack[-1] == '(':
                stack.pop()
            elif letter == '}' and stack[-1] == '{':
                stack.pop()
            elif letter == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(letter)

        return len(stack) == 0
            
