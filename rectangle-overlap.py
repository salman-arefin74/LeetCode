class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1 = rec1[0], rec1[1]
        ax2, ay2 = rec1[2], rec1[3]

        bx1, by1 = rec2[0], rec2[1]
        bx2, by2 = rec2[2], rec2[3]

        cx1 = max(ax1,bx1)
        cy1 = max(ay1,by1)
        cx2 = min(ax2,bx2)
        cy2 = min(ay2,by2)

        cl = cx2-cx1
        ch = cy2-cy1
        
        if cl > 0 and ch > 0:
            return True
            
        return False