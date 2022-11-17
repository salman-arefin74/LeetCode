class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1Area = (ax2-ax1)*(ay2-ay1)
        rec2Area = (bx2-bx1)*(by2-by1)
        
        cx1 = max(ax1,bx1)
        cy1 = max(ay1,by1)
        cx2 = min(ax2,bx2)
        cy2 = min(ay2,by2)

        cl = cx2-cx1
        ch = cy2-cy1
        cArea = 0

        if cl > 0 and ch > 0:
            cArea = cl * ch
        
        return rec1Area + rec2Area - cArea
