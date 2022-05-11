class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(' ')
        newWords = ""
        for x in words:
            if len(x) < 3:
                x = x.lower()
                newWords += x + " "
            else:
                x = x[0].upper() + x[1:].lower()
                newWords += x + " "

        return newWords.strip()