class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZeroMark = 0
        col_count, row_count = len(matrix[0]), len(matrix)
        for i in range(col_count):
            if matrix[0][i] ==0:
                rowZeroMark = -1
                break
        for i in range(row_count):
            if matrix[i][0] ==0:
                matrix[0][0] = 0
                break
        for i in range(1, col_count):
            for j in range(1, row_count):
                if matrix[j][i] ==0:
                    matrix[0][i] = 0
                    matrix[j][0] =0

        for i in range(1,col_count):
            if matrix[0][i] ==0:
                for j in range(row_count):
                    matrix[j][i] =0

        for i in range(1,row_count):
            if matrix[i][0] ==0:
                matrix[i] = [0] *col_count

        if matrix[0][0] ==0:
            for j in range(row_count):
                matrix[j][0] = 0
        
        if rowZeroMark ==-1:
            matrix[0] = [0] *col_count
        return matrix
