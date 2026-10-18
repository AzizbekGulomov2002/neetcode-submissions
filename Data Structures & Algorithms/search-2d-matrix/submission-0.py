class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search for row range
        top=0
        bottom=len(matrix)-1
        while top<=bottom:
            row=(top+bottom)//2
            if target<matrix[row][0]:
                bottom=row-1
            elif target>matrix[row][-1]:
                top=row+1
            else:
                break
        if top>bottom:
            return False

        # Binary search for selected row
        row = (top+bottom)//2
        left = 0
        right = len(matrix[row])-1
        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                left = mid+1
            else:
                right = mid-1
        return False