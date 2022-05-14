class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxCount = 0

        for x in sentences:
            split = x.split(' ')
            words = len(split)
            if words > maxCount:
                maxCount = words

        return maxCount