class Solution:
    def checkString(self, s: str) -> bool:
        valid = True

        for x in range(len(s)-1):
            if s[x] == 'b' and s[x+1] == 'a':
                valid = False
                break
        
        return valid