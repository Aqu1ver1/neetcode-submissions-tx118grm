class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:       
        rowsL,rowsR = 0, len(matrix) - 1
        rowsM = (rowsL + rowsR) // 2 
        while rowsL < rowsR:
            rowsM = (rowsL + rowsR) // 2  
            print(matrix[rowsM])
            if matrix[rowsM][0] > target:
                rowsR = rowsM - 1 
            elif matrix[rowsM][-1] < target:
                rowsL = rowsM + 1 
            else:
                break
        rowsM = (rowsL + rowsR) // 2 
        l,r = 0, len(matrix[rowsM])-1
        m = (l + r) // 2 
        while l < r:
            m = (l + r) // 2            
            if matrix[rowsM][m] > target:
                r = m - 1 
            elif matrix[rowsM][m] < target:
                l = m + 1 
            else:
                break
        m = (l + r) // 2  
        return matrix[rowsM][m] == target


                
        