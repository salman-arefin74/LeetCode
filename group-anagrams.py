class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempDict = {}
        result = []
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in tempDict:
                tempDict[sortedWord] = [word]
            else:
                tempDict[sortedWord].append(word)

        for subGroup in tempDict.values():
            result.append(subGroup)
        
        return result
