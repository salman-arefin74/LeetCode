class Solution(object):
    def maxDistance(self, colors):
        leftDistance = 0
        rightDistance = 0

        for x in range(len(colors)-1, 0, -1):
          if colors[0] != colors[x]:
            leftDistance = abs(0-x)
            break

        for x in range(0, len(colors)-1):
          if colors[len(colors)-1] != colors[x]:
            rightDistance = abs(len(colors)-1-x)
            break

        return max(leftDistance, rightDistance)
  
        