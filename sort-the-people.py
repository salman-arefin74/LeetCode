class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sortedNames = []

        for i in range(len(heights)):
          sortedNames.append([heights[i], names[i]])

        sortedNames.sort(reverse=True)

        return [name for height, name in sortedNames]