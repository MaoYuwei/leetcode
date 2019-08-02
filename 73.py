class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
        rows = list(set(rows))
        cols = list(set(cols))
        for r in rows:
            for k in range(n):
                matrix[r][k]=0
        for c in cols:
            for k in range(m):
                matrix[k][c]=0
        return matrix

if __name__ == '__main__':
    solution = Solution()
    print solution.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
])