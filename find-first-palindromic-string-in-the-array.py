class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        found = ""

        for x in words:
            reverse = x[::-1]
            if reverse == x:
                found = x
                break

        return found