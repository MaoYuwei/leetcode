class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        if len(matrix[0])==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        while row<m and matrix[row][-1]<target:
            row += 1
        # print row
        if row==m:
            return False
        col = 0
        while col<n and matrix[row][col]<target:
            col += 1
        if matrix[row][col]==target:
            return True
        return False
if __name__ == '__main__':
    solution = Solution()
    print solution.searchMatrix(matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],
target = 3)