class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        wordList = wordList[::-1]
        
        return ' '.join(wordList)