class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]
        if numRows ==1:
            return tri
        for i in range(1, numRows):
            parent_row = tri[-1]
            parent_row = [0] + parent_row + [0]
            new_row = [parent_row[i] + parent_row[i-1] for i in range(1,len(parent_row))]
            tri.append(new_row)
        return tri
