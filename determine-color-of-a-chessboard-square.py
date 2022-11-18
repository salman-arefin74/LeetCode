class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (coordinates[0] == 'a' or coordinates[0] == 'c' or coordinates[0] == 'e' or coordinates[0] == 'g') and (int(coordinates[1]) %2 == 0):
            return True
        if (coordinates[0] == 'b' or coordinates[0] == 'd' or coordinates[0] == 'f' or coordinates[0] == 'h') and (int(coordinates[1]) %2 != 0):
            return True
        else: 
            return False  