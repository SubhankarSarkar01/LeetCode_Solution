# -- 54. Spiral Matrix --
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startRow = 0
        startCol = 0
        endRow = len(matrix)-1
        endCol = len(matrix[0])-1
        res = []
        while (startRow<=endRow and startCol <=endCol):
            # Top
            for j in range(startCol,endCol+1,1):
                res.append(matrix[startRow][j])

            # Right
            for i in range(startRow+1,endRow+1,1):
                res.append(matrix[i][endCol])
            
            # Bottom
            for j in range(endCol-1,startCol-1,-1):
                if(startRow == endRow):
                    break
                res.append(matrix[endRow][j])
            
            # left
            for i in range(endRow-1,startRow,-1):
                if (startCol == endCol):
                    break
                res.append(matrix[i][startCol])

            
            startCol = startCol + 1
            startRow = startRow + 1
            endCol = endCol - 1
            endRow = endRow -1

            
        return res
            
                

        