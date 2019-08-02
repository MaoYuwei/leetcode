class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = grid[0][0]
        m = len(grid)
        n = len(grid[0])
        dp = [[x for _ in range(n)] for _ in range(m)]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]+grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]

        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    print solution.minPathSum([[1,2],[5,6],[1,1]])