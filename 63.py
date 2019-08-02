class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[1 for _ in range(n)] for _ in range(m)]

        if obstacleGrid[0][0]==1:
            matrix[0][0]=0

        for j in range(1, n):
            if matrix[0][j-1]==0 or obstacleGrid[0][j]==1:
                matrix[0][j] = 0

        # print matrix

        for i in range(1, m):
            if matrix[i-1][0]==0 or obstacleGrid[i][0]==1:
                matrix[i][0]=0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
        # print matrix
        return matrix[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    print solution.uniquePathsWithObstacles([[1,0]])
